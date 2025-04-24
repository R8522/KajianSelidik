import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Analisis Perpustakaan", layout="wide")

# --- Tajuk Besar ---
st.markdown("<h1 style='text-align: center;'>📚 Analisis Penutupan Perpustakaan Bukit Merah</h1>", unsafe_allow_html=True)

# --- Load CSV ---
data = pd.read_csv('Desa sempeneh.csv')

# --- Ringkasan ---
st.markdown("### 📥 Data Asal")
st.write("Jumlah responden:", data.shape[0])
st.dataframe(data)

st.markdown("### 📌 Nilai Kosong")
st.write(data.isnull().sum())

st.markdown("### 📊 Statistik Ringkas")
st.write(data.describe())

# --- Visualization Header ---
st.markdown("<h2 style='text-align: center;'>📈 Visualisasi Data</h2>", unsafe_allow_html=True)
