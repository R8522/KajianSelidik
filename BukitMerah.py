import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Title ---
st.set_page_config(page_title="Analisis Perpustakaan", layout="wide")
st.title("📚 Analisis Penutupan Perpustakaan Bukit Merah")

# --- Load CSV ---
data = pd.read_csv('BukitMerah.csv')

# --- Ringkasan ---
st.subheader("📥 Data Asal")
st.write("Jumlah responden:", data.shape[0])
st.dataframe(data)

st.subheader("📌 Nilai Kosong")
st.write(data.isnull().sum())

st.subheader("📊 Statistik Ringkas")
st.write(data.describe())

# --- Visualization ---
st.header("📈 Visualisasi Data")

def plot_grouped_line(column, title):
    grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    for col in grouped.columns:
        ax.plot(grouped.index, grouped[col], marker='o', label=col)
    ax.set_xlabel('Kumpulan Umur')
    ax.set_ylabel('Bilangan Responden')
    ax.set_title(title)
    ax.legend(title=column)
    ax.grid(True, linestyle='--', alpha=0.4)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def plot_grouped_bar(column, title):
    grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    grouped.plot(kind='bar', ax=ax, width=0.5)
    ax.set_xlabel('Kumpulan Umur')
    ax.set_ylabel('Bilangan Responden')
    ax.set_title(title)
    ax.legend(title=column)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

# --- User Control ---
if st.checkbox("📍 Penutupan Perpustakaan"):
    plot_grouped_line('Penutupan_perpustakaan', 'Respon vs Penutupan Perpustakaan')

if st.checkbox("📍 Lokasi Strategik"):
    plot_grouped_line('Lokasi_strategik', 'Umur vs Lokasi Strategik')

if st.checkbox("📍 Keperluan Perpustakaan"):
    plot_grouped_line('Keperluan_perpustakaan', 'Umur vs Keperluan Perpustakaan')

if st.checkbox("📍 Kekurangan Pengunjung"):
    plot_grouped_line('Kekurangan_pengunjung', 'Bilangan Responden vs Kekurangan Pengunjung')

if st.checkbox("📍 Operasi Perpustakaan"):
    plot_grouped_line('Operasi_perpustakaan', 'Bilangan Responden vs Pengoperasian')

if st.checkbox("📍 Histogram Jarak Lokasi"):
    plot_grouped_bar('Jarak_lokasi', 'Histogram: Bilangan Responden vs Jarak Lokasi')
