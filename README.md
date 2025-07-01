# 📄 PDF Scraper App with Streamlit

A smart web-based tool for extracting **tables or text** from PDF documents using **page numbers, ranges, or even keywords**. Built with real-world pain, for real-world use.

👉 Try the live app here: [pdfscrapper.streamlit.app](https://pdfscrapper.streamlit.app)

---

## 🚀 Features

✅ Upload or paste a URL to any PDF  
✅ Extract **tables or text**  
✅ Use **keywords** (like "Revenue") to auto-find pages  
✅ Specify page ranges (e.g., `5:20`) or list (`1, 3, 8`)  
✅ **OCR support** for scanned PDFs  
✅ Export results as **CSV**, **Excel**, or **JSON**

---

## 🧠 Why This Exists

This project was born from the frustration of searching through 900+ page budget books to find a single table. If you’ve ever tried to copy-paste data from a government PDF, you know the pain. This app solves that.

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) — UI Framework  
- [pdfplumber](https://github.com/jsvine/pdfplumber) — Table and text extraction  
- [PyMuPDF (fitz)](https://github.com/pymupdf/PyMuPDF) — Keyword page search  
- [pytesseract](https://github.com/madmaze/pytesseract) — OCR for scanned documents  
- [pdf2image](https://github.com/Belval/pdf2image) — Image conversion for OCR  
- [pandas](https://pandas.pydata.org/) — Data wrangling

---

## 🗂️ Project Structure

pdf_scraper_app/

├── app.py # Streamlit app UI

├── requirements.txt # Project dependencies

├── .streamlit/

│ └── config.toml # Theme + file size settings

├── utils/

│ ├── file_utils.py # Download + file handling

│ ├── page_utils.py # Keyword/page logic

│ ├── table_extraction.py # Table parsing logic

│ └── text_extraction.py # Text + OCR logic


---

## 🛠️ Setup & Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/KiruruKamau/Pdf_scrapper.git
cd pdf-scraper-app
pip install -r requirements.txt
streamlit run app.py
📝 If you need larger file uploads (like 100MB PDFs), make sure .streamlit/config.toml includes:
[server]
maxUploadSize = 100

🧪 Example Use Cases
Extract vote-level estimates from national budgets

Search “Revenue” in public expenditure books

Scrape text from scanned archival documents

Turn PDF tables into datasets with zero code

🙌 Contributions
Got ideas for improvement or want to collaborate? Feel free to fork or open an issue.

📬 Contact
Connect with me on kamaukiruru@gmail.com

📝 License
MIT — use it, build on it, just don’t sell it as-is.






