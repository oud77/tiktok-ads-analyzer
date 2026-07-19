import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Goldenday", layout="wide")

st.title("📊 Dashboard Profit Goldenday")

# ID Google Sheet Anda
SHEET_ID = "19_aTelubx5W7CEjRPZYF_SDKVD8516CkwjRWirhRUac"
SHEET_NAME = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

try:
    df = pd.read_csv(url)
    st.success("Data berhasil dimuat!")
    
    # Hitung total omzet
total_omzet = df['total omzet (pendapatan)'].sum()   
st.metric("Total Omzet Keseluruhan", f"Rp {total_omzet:,}")
    
    st.write("### Data Harian Anda")
    st.dataframe(df)
    
except Exception as e:
    st.error("Gagal memuat data. Pastikan Google Sheet Anda diatur ke 'Anyone with the link can view' dan nama sheet benar.")
