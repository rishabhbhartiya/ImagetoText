import pytesseract
from PIL import Image
import streamlit as st


st.title("OPTICAL CHARACTER RECOGNITION")

# File uploader for image
img_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if img_file is not None:
    img = Image.open(img_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Perform OCR using pytesseract
    ocr_result = pytesseract.image_to_string(img)
    st.subheader("OCR Result")
    st.text(ocr_result)