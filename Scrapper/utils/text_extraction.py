import pdfplumber
import pytesseract
import pdf2image
import tempfile

def extract_text(pdf_file, pages):
    lines = []
    with pdfplumber.open(pdf_file) as pdf:
        for page_num in pages:
            page = pdf.pages[page_num - 1]
            text = page.extract_text()
            lines.append(text)
    return lines

def extract_text_with_ocr(pdf_bytes, pages):
    temp_dir = tempfile.mkdtemp()
    images = pdf2image.convert_from_bytes(
        pdf_bytes, first_page=min(pages), last_page=max(pages), output_folder=temp_dir
    )
    texts = [pytesseract.image_to_string(img) for img in images]
    return texts
