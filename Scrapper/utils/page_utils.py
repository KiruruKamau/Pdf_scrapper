import fitz  # PyMuPDF

def find_pages_with_keyword(pdf_path_or_bytes, keyword):
    doc = fitz.open(stream=pdf_path_or_bytes, filetype="pdf")
    matching_pages = []
    for i in range(len(doc)):
        text = doc[i].get_text()
        if keyword.lower() in text.lower():
            matching_pages.append(i + 1)  # 1-based
    return matching_pages
