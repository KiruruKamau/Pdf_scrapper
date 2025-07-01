import pandas as pd
import pdfplumber
from collections import Counter

def make_unique_columns(columns):
    seen = Counter()
    new_columns = []
    for col in columns:
        count = seen[col]
        new_col = col if count == 0 else f"{col}_{count}"
        new_columns.append(new_col)
        seen[col] += 1
    return new_columns

def extract_tables(pdf_file, pages):
    dataframes = []
    with pdfplumber.open(pdf_file) as pdf:
        for page_num in pages:
            page = pdf.pages[page_num - 1]
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=make_unique_columns(table[0]))
                dataframes.append(df)
    return dataframes
