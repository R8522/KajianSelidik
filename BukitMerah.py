import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Analisis Perpustakaan", layout="wide")

# --- Tajuk Besar ---
st.markdown("<h1 style='text-align: center;'>📚 Analisis Penutupan Perpustakaan Bukit Merah</h1>", unsafe_allow_html=True)

# --- Load CSV ---
data = pd.read_csv('BukitMerah.csv')

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

# --- Function: Line Chart ---
def plot_grouped_line(column, title):
    grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(7, 5))  # <<< saiz kecil

    for col in grouped.columns:
        ax.plot(grouped.index, grouped[col], marker='o', label=col, markersize=4)  # <<< kecilkan marker

    ax.set_xlabel('Kumpulan Umur', fontsize=10)
    ax.set_ylabel('Bilangan Responden', fontsize=10)
    ax.set_title(title, fontsize=12)
    ax.legend(title=column, fontsize=8, title_fontsize=9, loc='upper left')  # <<< kecilkan legend
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45, fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    # Center grafik
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig)

# --- Function: Bar Chart ---
def plot_grouped_bar(column, title):
    grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(7, 4))
    grouped.plot(kind='bar', ax=ax, width=0.8)

    ax.set_xlabel('Kumpulan Umur')
    ax.set_ylabel('Bilangan Responden')
    ax.set_title(title)
    ax.legend(title=column)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Center grafik
    col2, col3 = st.columns([1,1])
    with col2:
        st.pyplot(fig)

# --- User Controls ---
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
