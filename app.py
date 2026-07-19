import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Profit Goldenday", layout="wide")

st.title("📊 Dashboard Profit Goldenday")

SHEET_ID = "19_aTelubx5W7CEjRPZYF_SDKVD8516CkwjRWirhRUac"
SHEET_NAME = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

try:
    df = pd.read_csv(url)
    
    # Membersihkan nama kolom (menghapus spasi di awal/akhir)
    df.columns = df.columns.str.strip().str.lower()
    
    # Perhitungan Profit (pastikan nama kolom sudah sesuai)
    df['profit bersih'] = df['total omzet (pendapatan)'] - df['biaya iklan'] - df['hpp produk']
    
    total_omzet = df['total omzet (pendapatan)'].sum()
    total_profit = df['profit bersih'].sum()
    
    col1, col2 = st.columns(2)
    col1.metric("Total Omzet", f"Rp {total_omzet:,.0f}")
    col2.metric("Total Profit Bersih", f"Rp {total_profit:,.0f}")
    
    st.write("### Detail Data Harian")
    st.dataframe(df)
    
    st.write("### Tren Profit Bersih")
    st.line_chart(df.set_index('tanggal')['profit bersih'])
    
except Exception as e:
    st.error(f"Error: {e}. Pastikan baris pertama Google Sheet berisi: tanggal, produk, jumlah terjual, total omzet (pendapatan), biaya iklan, hpp produk")
