# Image Text Extraction and Categorization Project

## Overview

This project involves extracting text from an image, splitting the image into patches, performing Optical Character Recognition (OCR) using Tesseract, and categorizing the extracted text into predefined sections based on gland names. The goal is to organize the information in the image into a structured dictionary format.

## Features

- **Image Patching**: The image is split into smaller sections to improve OCR accuracy.
- **Text Extraction with Tesseract**: Uses `pytesseract` to extract text from the patches.
- **Text Categorization**: Extracted text is categorized into gland names and their associated hormones or descriptions.
- **Printed Output**: Both the full extracted text and the categorized output are printed for review.

## Approaches Followed

### 1. **Splitting the Image into Patches**
   - The image is divided into multiple smaller patches (4x2 grid) to handle large images or images with dense text better.
   - This approach increases OCR accuracy by reducing the amount of text processed at a time and minimizing distortions from scaling.

### 2. **Optical Character Recognition (OCR)**
   - We use `pytesseract`, which is the Python wrapper for Google Tesseract OCR, to extract text from each image patch.
   - The extracted text is cleaned using regular expressions to remove extra spaces or line breaks.

### 3. **Text Categorization**
   - The extracted text is split and categorized using predefined gland headers.
   - Regular expressions are used to match gland names, and the corresponding text is assigned as the description or hormones for that gland.

## Project Structure

- **`gland_headers`**: A list of gland names that will be used to categorize the extracted text.
- **`hormone_data`**: A dictionary where the keys are gland names, and the values are extracted text related to those glands.
- **Functions**:
  - `split_image_into_patches()`: Splits the input image into smaller patches.
  - `extract_text_from_patch()`: Extracts text from each patch using `pytesseract`.
  - `categorize_text()`: Categorizes the extracted text based on gland names.
  - `main()`: The main function that orchestrates the entire process from image splitting to text extraction and categorization.

## Requirements

The following Python libraries are required to run the code:

```bash
pip install pytesseract
pip install Pillow
```
# Example Input and Output

## Sample Input

```bash
Enter Image Path: /Users/ujjwalraj/Desktop/sample.jpeg
```

# Sample Output
{
    "Hypothalamus": "TRH, CRH, GHRH, Dopamine, Somatostatin, Vasopressin",
    "Thyroid and Parathyroid": "T3, T4, Calcitonin, PTH",
    "Liver": "GH, TSH, ACTH, FSH, MSH, LH, Prolactin, Oxytocin, Vasopressin",
    "Adrenal": "Adrenaline, Noradrenaline",
    "Kidney": "",
    "Testes": "Androgens, Estradiol, Inhibin, Somatostatin",
    "Pineal Gland": "Melatonin",
    "Pituitary gland": "",
    "Thymus": "Thymopoietin, IGF, THPO",
    "Stomach": "Gastrin, Ghrelin, Histamine, Somatostatin, Neuropeptide Y",
    "Pancreas": "Insulin, Glucagon",
    "Ovary, Placenta": "Estrogens, Progesterone",
    "Uterus": "Prolactin, Relaxin"
}
