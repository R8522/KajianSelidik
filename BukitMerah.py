import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Perpustakaan", layout="wide")

# --- Sidebar Navigation ---
location = st.sidebar.selectbox("Pilih Lokasi", ["Bukit Merah", "Desa Sempeneh"])

if location == "Bukit Merah":
    # --- Tajuk Besar ---
    st.markdown("<h1 style='text-align: center;'>📚 Analisis Penutupan Perpustakaan Bukit Merah</h1>", unsafe_allow_html=True)

    # --- Load CSV ---
    data = pd.read_csv('BukitMerah.csv')

    # --- Ringkasan Data ---
    st.markdown("### 📥 Data Asal")
    st.write("Jumlah responden:", data.shape[0])
    st.dataframe(data)

    st.markdown("### 📌 Nilai Kosong")
    st.write(data.isnull().sum())

    st.markdown("### 📊 Statistik Ringkas")
    st.write(data.describe())

    st.markdown("<h2 style='text-align: center;'>📈 Visualisasi Data</h2>", unsafe_allow_html=True)

    # --- Function to center content ---
    def center_content(plot_func):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            plot_func()

    # --- Visualization Function ---
    def plot_grouped_line(column, title):
        def draw():
            grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
            fig, ax = plt.subplots(figsize=(7, 5))
            for col in grouped.columns:
                ax.plot(grouped.index, grouped[col], marker='o', label=col, markersize=4)
            ax.set_xlabel('Kumpulan Umur')
            ax.set_ylabel('Bilangan Responden')
            ax.set_title(title)
            ax.legend(title=column)
            ax.grid(True, linestyle='--', alpha=0.5)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        center_content(draw)

    def plot_grouped_bar(column, title):
        def draw():
            grouped = data.groupby(['Umur', column]).size().unstack(fill_value=0)
            fig, ax = plt.subplots(figsize=(7, 5))
            grouped.plot(kind='bar', ax=ax, width=0.8)
            ax.set_title(title)
            ax.set_xlabel("Kumpulan Umur")
            ax.set_ylabel("Bilangan Responden")
            ax.grid(True, axis='y', linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        center_content(draw)

    # --- Controls ---
    if st.checkbox("📍 Penutupan Perpustakaan"):
        plot_grouped_line('Penutupan_perpustakaan', 'Umur vs Penutupan Perpustakaan')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan jawapan penutupan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Penutupan_perpustakaan'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada penutupan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Penutupan_perpustakaan'].value_counts().to_frame(name='Jumlah')))

    if st.checkbox("📍 Lokasi Strategik"):
        plot_grouped_line('Lokasi_strategik', 'Umur vs Lokasi Strategik')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Lokasi_strategik'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Lokasi_strategik'].value_counts().to_frame(name='Jumlah')))



