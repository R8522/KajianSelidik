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
        ax.plot(grouped.index, grouped[col], marker='o', label=col, markersize=4)  

    ax.set_xlabel('Kumpulan Umur', fontsize=10)
    ax.set_ylabel('Bilangan Responden', fontsize=10)
    ax.set_title(title, fontsize=12)
    ax.legend(title=column, fontsize=8, title_fontsize=9, loc='upper left') 
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45, fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
   

    # Center grafik
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig)

# --- Function: Bar Chart ---
def plot_grouped_bar(column, title):
    grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(7, 5))
    grouped.plot(kind='bar', ax=ax, width=0.8)

    ax.set_xlabel('Kumpulan Umur')
    ax.set_ylabel('Bilangan Responden')
    ax.set_title(title)
    ax.legend(title=column)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Center grafik
    col1,col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig)

# --- User Controls ---
if st.checkbox("📍 Penutupan Perpustakaan"):
    plot_grouped_line('Penutupan_perpustakaan', 'Respon vs Penutupan Perpustakaan')
    
    st.subheader("Bilangan responden ikut umur dan jawapan penutupan")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.dataframe(
            data.groupby('Umur')['Penutupan_perpustakaan']
                .value_counts()
                .unstack(fill_value=0)
        )

    st.subheader("Jumlah keseluruhan respon kepada penutupan")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.dataframe(
            data['Penutupan_perpustakaan']
                .value_counts()
                .to_frame(name='Jumlah')
        )


if st.checkbox("📍 Lokasi Strategik"):
    plot_grouped_line('Lokasi_strategik', 'Umur vs Lokasi Strategik')
    st.subheader("Bilangan responden ikut umur dan Lokasi")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data.groupby('Umur')['Lokasi_strategik'].value_counts())
    
    st.subheader("Jumlah keseluruhan respon kepada penutupan")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data['Lokasi_strategik'].value_counts())

if st.checkbox("📍 Keperluan Perpustakaan"):
    plot_grouped_line('Keperluan_perpustakaan', 'Umur vs Keperluan Perpustakaan')
    st.subheader("Bilangan responden ikut umur dan keperluan perpustakaan")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data.groupby('Umur')['Keperluan_perpustakaan'].value_counts())
    
    st.subheader("Jumlah keseluruhan respon keperluan perpustakaan")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data['Keperluan_perpustakaan'].value_counts())

if st.checkbox("📍 Kekurangan Pengunjung"):
    plot_grouped_line('Kekurangan_pengunjung', 'Bilangan Responden vs Kekurangan Pengunjung')
    st.subheader("Bilangan responden ikut umur dan  kekurangan pengunjung")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data.groupby('Umur')['Kekurangan_pengunjung'].value_counts())
    
    st.subheader("Jumlah keseluruhan respon kekurangan pengunjung")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data['Penutupan_perpustakaan'].value_counts())

if st.checkbox("📍 Operasi Perpustakaan"):
    plot_grouped_line('Operasi_perpustakaan', 'Bilangan Responden vs Pengoperasian')
    st.subheader("Bilangan responden ikut umur dan penoperasian")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data.groupby('Umur')['Operasi_perpustakaan'].value_counts())
    
    st.subheader("Jumlah keseluruhan respon pengoperasian")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data['Operasi_perpustakaan'].value_counts())

if st.checkbox("📍 Histogram Jarak Lokasi"):
    plot_grouped_bar('Jarak_lokasi', 'Histogram: Bilangan Responden vs Jarak Lokasi')
    st.subheader("Bilangan responden ikut umur dan jarak lokasi")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data.groupby('Umur')['Jarak_lokasi'].value_counts())
    
    st.subheader("Jumlah keseluruhan respon jarak lokasi")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
    st.write(data['Jarak_lokasi'].value_counts())
