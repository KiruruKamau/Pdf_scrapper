# app.py
import streamlit as st
import pandas as pd
from io import BytesIO

from utils.file_utils import download_pdf
from utils.page_utils import find_pages_with_keyword
from utils.table_extraction import extract_tables
from utils.text_extraction import extract_text, extract_text_with_ocr

# === Streamlit UI ===
st.set_page_config(page_title="PDF Table/Text Scraper")
st.title("📄 PDF Table/Text Scraper with Streamlit")

pdf_bytes = None
st.markdown("### 🧾 Input Options")
option = st.radio("Choose input method:", ["Upload PDF", "Enter PDF URL"])

if option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        if uploaded_file.size > 100 * 1024 * 1024:
            st.error("File too large. Please upload a file under 100MB.")
        else:
            pdf_bytes = uploaded_file.read()
else:
    pdf_url = st.text_input("Enter PDF URL")
    pdf_bytes = download_pdf(pdf_url) if pdf_url else None

if pdf_bytes:
    st.markdown("---")
    st.markdown("### ⚙️ Extraction Settings")
    method = st.radio("What do you want to extract?", ["Tables", "Text"])
    page_input = st.text_input("Enter pages (e.g., 1,2,3 or 5:20 or keyword like 'Revenue')", value="all")
    export_format = st.selectbox("Export format", ["CSV", "Excel", "JSON"])
    use_ocr = st.checkbox("Use OCR if text extraction fails (for scanned PDFs)")
    extract_button = st.button("Extract")

    if extract_button:
        with st.spinner("Extracting data..."):
            pages = []
            if page_input.lower() == "all":
                import pdfplumber
                with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
                    pages = list(range(1, len(pdf.pages) + 1))
            elif ":" in page_input:
                try:
                    start, end = map(int, page_input.split(":"))
                    pages = list(range(start, end + 1))
                except:
                    st.error("Invalid range format. Use start:end")
            elif page_input.replace(",", "").isdigit():
                pages = [int(p.strip()) for p in page_input.split(",") if p.strip().isdigit()]
            else:
                pages = find_pages_with_keyword(pdf_bytes, page_input)

            if not pages:
                st.warning("No pages found matching that input.")
            else:
                st.success(f"Extracting from pages: {pages}")

                if method == "Tables":
                    dfs = extract_tables(BytesIO(pdf_bytes), pages)
                    if dfs:
                        for i, df in enumerate(dfs):
                            st.subheader(f"Table {i+1}")
                            st.dataframe(df)
                        try:
                            final_df = pd.concat(dfs, ignore_index=True)
                            if export_format == "CSV":
                                data = final_df.to_csv(index=False).encode("utf-8")
                                st.download_button("Download CSV", data, "tables_output.csv", "text/csv")
                            elif export_format == "Excel":
                                excel_data = BytesIO()
                                final_df.to_excel(excel_data, index=False, engine='openpyxl')
                                st.download_button("Download Excel", excel_data.getvalue(), "tables_output.xlsx")
                            elif export_format == "JSON":
                                json_data = final_df.to_json(orient="records").encode("utf-8")
                                st.download_button("Download JSON", json_data, "tables_output.json")
                        except Exception as e:
                            st.error(f"Error combining tables: {e}")
                    else:
                        st.warning("No tables found on those pages.")

                elif method == "Text":
                    texts = extract_text(BytesIO(pdf_bytes), pages)
                    if not any(texts) and use_ocr:
                        texts = extract_text_with_ocr(pdf_bytes, pages)
                    final_text = "\n\n".join(texts)
                    st.text_area("Extracted Text", final_text, height=300)

                    df_text = pd.DataFrame({"Text": texts})
                    if export_format == "CSV":
                        csv = df_text.to_csv(index=False).encode("utf-8")
                        st.download_button("Download CSV", csv, "text_output.csv", "text/csv")
                    elif export_format == "Excel":
                        excel_data = BytesIO()
                        df_text.to_excel(excel_data, index=False, engine='openpyxl')
                        st.download_button("Download Excel", excel_data.getvalue(), "text_output.xlsx")
                    elif export_format == "JSON":
                        json_data = df_text.to_json(orient="records").encode("utf-8")
                        st.download_button("Download JSON", json_data, "text_output.json")
