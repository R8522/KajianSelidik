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
        st.markdown(""" Sebanyak 52% responden memilih untuk tidak perlu menutup perpustakaan di Desa Bukit Merah  """)

    if st.checkbox("📍 Lokasi Strategik"):
        plot_grouped_line('Lokasi_strategik', 'Umur vs Lokasi Strategik')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Lokasi_strategik'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Lokasi_strategik'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 58% responden mengundi bahawa lokasi perpustakaan bagi Bukit Merah adalah tidak strategik. """)
    
    if st.checkbox("📍 Kekurangan Pengunjung"):
        plot_grouped_line('Kekurangan_pengunjung', 'Umur vs  Kekurangan Pengunjung')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan Kekurangan pengunjung</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Kekurangan_pengunjung'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada kekurangan pengunjung</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Kekurangan_pengunjung'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 88% responden mengatakakan bahawa Desa Bukit Merah mempunyai kurang pengujung """)
    
    if st.checkbox("📍 Keperluan Perpustakaan"):
        plot_grouped_line('Keperluan_perpustakaan', 'Bilangan Responden vs Keperluan Perpustakaan')
        st.markdown("### <div style='text-align: center;'>Bilangan responden daripada soalan keperluan perpustakaan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Keperluan_perpustakaan'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon keperluan perpustakaan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Keperluan_perpustakaan'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 77% responden mengatakakan bahawa keperluan perpustakaan di Desa Sempeneh adalah perlu di desa tersebut. """)
    
    if st.checkbox("📍 Operasi perpustakaan"):
        plot_grouped_line('Operasi_perpustakaan', 'Bilangan Responden vs Pengoperasian')
        st.markdown("### <div style='text-align: center;'>Bilangan Responden vs Pengoperasian</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Operasi_perpustakaan'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon pengoperasian</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Operasi_perpustakaan'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 60% responden mengatakakan bahawa operasi bagi perpustakaan di Desa Bukit Merah adalah perlu diteruskan. """)
    
    if st.checkbox("📍 Jarak Lokasi"):
        plot_grouped_bar('Jarak_lokasi', 'Histogram: Bilangan Responden vs Jarak lokasi')
        st.markdown("### <div style='text-align: center;'>Bilangan Responden vs Jarak Lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Jarak_lokasi'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon jarak lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Jarak_lokasi'].value_counts().to_frame(name='Jumlah')))



st.markdown(""" Kesimpulannya, perpustakaan desa bagi Bukit Merah adalah tidak perlu ditutup. Isu utama mungkin adalah disebabkan oleh lokasi yang tidak strategik dan mungkin juga disebabkan oleh keperluan lain yang tidak mencukupi. """)

if location == "Desa Sempeneh":
    # --- Tajuk Besar ---
    st.markdown("<h1 style='text-align: center;'>📚 Analisis Penutupan Perpustakaan Desa Sempeneh</h1>", unsafe_allow_html=True)

    # --- Load CSV & Drop Nulls ---
    data = pd.read_csv('Desa sempeneh.csv')
    data.dropna(inplace=True)  # Hapus baris dengan nilai kosong

    # --- Ringkasan Data ---
    st.markdown("### 📥 Data Asal")
    st.write("Jumlah responden selepas buang nilai kosong:", data.shape[0])
    st.dataframe(data)

    st.markdown("### 📌 Nilai Kosong (Selepas Buang)")
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
        plot_grouped_line('Penutupan_perpustakaan', 'Respon vs Penutupan Perpustakaan')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan jawapan penutupan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Penutupan_perpustakaan'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada penutupan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Penutupan_perpustakaan'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 83% responden mengatakakan bahawa perpustakaan bagi Desa Sempeneh adalah perlu ditutup """)

    if st.checkbox("📍 Lokasi Strategik"):
        plot_grouped_line('Lokasi_strategik', 'Umur vs Lokasi Strategik')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Lokasi_strategik'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Lokasi_strategik'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 67% responden mengatakakan bahawa lokasi di perpustakaan Desa Sempeneh adalah tidak strategik """)
    
    if st.checkbox("📍 Kekurangan Pengunjung"):
        plot_grouped_line('Kekurangan_pengunjung', 'Umur vs  Kekurangan Pengunjung')
        st.markdown("### <div style='text-align: center;'>Bilangan responden ikut umur dan kekurangan pengunjung</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Kekurangan_pengunjung'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon kepada kekurangan pengunjung</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Kekurangan_pengunjung'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 58% responden mengatakakan bahawa perpustakaan di Desa Sempeneh mempunyai ramai pengujung """)
    
    if st.checkbox("📍 Keperluan Perpustakaan"):
        plot_grouped_line('Perlu_ada', 'Bilangan Responden vs Keperluan Perpustakaan')
        st.markdown("### <div style='text-align: center;'>Bilangan responden daripada soalan keperluan perpustakaan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Perlu_ada'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon keperluan perpustakaan</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Perlu_ada'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 70% responden mengatakakan bahawa keperluan perpustakaan di Desa Sempeneh adalah tidak perlu """)
    
    if st.checkbox("📍 Operasi perpustakaan"):
        plot_grouped_line('Operasi', 'Bilangan Responden vs Pengoperasian')
        st.markdown("### <div style='text-align: center;'>Bilangan Responden vs Pengoperasian</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Operasi'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon pengoperasian</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Operasi'].value_counts().to_frame(name='Jumlah')))
        st.markdown(""" Sebanyak 70% responden mengatakakan bahawa operasi bagi perpustakaan di Desa Sempeneh adalah tidak perlu diteruskan. """)
    
    if st.checkbox("📍 Jarak Lokasi"):
        plot_grouped_bar('Jarak_lokasi', 'Histogram: Bilangan Responden vs Jarak lokasi')
        st.markdown("### <div style='text-align: center;'>Bilangan Responden vs Jarak Lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data.groupby('Umur')['Jarak_lokasi'].value_counts().unstack(fill_value=0)))
        st.markdown("### <div style='text-align: center;'>Jumlah keseluruhan respon jarak lokasi</div>", unsafe_allow_html=True)
        center_content(lambda: st.dataframe(data['Jarak_lokasi'].value_counts().to_frame(name='Jumlah')))



    st.markdown(""" Kesimpulannya, perpustakaan bagi Desa Sempeneh adalah perlu ditutup """)
