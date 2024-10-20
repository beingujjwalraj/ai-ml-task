import pytesseract
from PIL import Image
import re

# Define the gland headers as keys for the dictionary
gland_headers = [
    "Hypothalamus", "Thyroid and Parathyroid", "Liver", "Adrenal", 
    "Kidney", "Testes", "Pineal Gland", "Pituitary gland", 
    "Thymus", "Stomach", "Pancreas", "Ovary, Placenta", "Uterus"
]

# Initialize the expected output structure
hormone_data = {header: "" for header in gland_headers}

# Function to divide the image into patches
def split_image_into_patches(image, rows, cols):
    """
    Splits the image into patches by dividing it into a grid.
    :param image: PIL Image object
    :param rows: Number of rows to split
    :param cols: Number of columns to split
    :return: List of patches
    """
    img_width, img_height = image.size
    patch_width = img_width // cols
    patch_height = img_height // rows

    patches = []
    for i in range(rows):
        for j in range(cols):
            left = j * patch_width
            top = i * patch_height
            right = (j + 1) * patch_width
            bottom = (i + 1) * patch_height
            patch = image.crop((left, top, right, bottom))
            patches.append(patch)
    
    return patches

# Function to extract text from an image patch using pytesseract
def extract_text_from_patch(patch):
    """
    Extracts text from a patch using pytesseract.
    """
    text = pytesseract.image_to_string(patch)
    
    # Clean up the text by removing extra newlines and multiple spaces
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces/newlines with a single space
    return text

# Function to categorize the text based on gland headers
def categorize_text(extracted_text, gland_headers):
    """
    Categorizes the extracted text into the predefined categories.
    Each gland header is treated as a key, and the associated hormones are added as values.
    """
    current_key = None

    # Create a regex pattern to match gland headers
    gland_pattern = '|'.join(map(re.escape, gland_headers))

    # Split the text into chunks based on gland headers
    sections = re.split(f"({gland_pattern})", extracted_text)

    for i, section in enumerate(sections):
        section = section.strip()
        
        # If the section is a known gland, set it as the current key
        if section in gland_headers:
            current_key = section
        elif current_key and section:
            # Check if section is not another gland
            if section not in gland_headers:
                # Add the section to the current key (assumed to be the hormones)
                # Strip any extra spaces and commas
                hormones = section.strip(", ")
                hormone_data[current_key] = hormones

    return hormone_data

# Main function to handle the entire process
def main(image_path):
    """
    Main function that splits the image into patches, extracts text from each patch, 
    and structures it into a dictionary.
    """
    # Load the image
    img = Image.open(image_path)

    # Step 1: Split the image into patches (4x2 grid)
    patches = split_image_into_patches(img, rows=4, cols=2)

    # Step 2: Extract text from each patch and concatenate it
    full_text = ""
    for patch in patches:
        patch_text = extract_text_from_patch(patch)
        print(f"Extracted Text from Patch:\n{patch_text}\n")  # Print the extracted text from each patch
        full_text += patch_text + " "

    # Step 3: Categorize the extracted text
    categorized_output = categorize_text(full_text, gland_headers)
    
    return full_text, categorized_output

# Sample usage
image_file = input('Enter Image Path: ')  # Path to your image file
extracted_text, output = main(image_file)

# Output the extracted text and categorized dictionary
print("\nFull Extracted Text:\n", extracted_text)
print("\nCategorized Dictionary:\n", output)



