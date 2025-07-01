import requests
from io import BytesIO
import streamlit as st

def download_pdf(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            st.error(f"Failed to download PDF. Status: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Download error: {e}")
        return None
