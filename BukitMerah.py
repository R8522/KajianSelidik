import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
st.title("📊 Analisis Penutupan Perpustakaan Bukit Merah")
data = pd.read_csv("BukitMerah.csv")

st.subheader("🔍 Statistik Ringkas")
st.write(data.describe())
st.write("Jumlah nilai kosong setiap kolum:")
st.write(data.isnull().sum())

# ========================
# 1. Penutupan Perpustakaan
# ========================
st.subheader("📌 Respon vs Penutupan Perpustakaan")
grouped = data.groupby(['Umur', 'Penutupan_perpustakaan']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
for col in grouped.columns:
    ax.plot(grouped.index, grouped[col], marker='o', label=col)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Respon vs Penutupan Perpustakaan")
ax.legend(title="Penutupan_perpustakaan")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# ========================
# 2. Lokasi Strategik
# ========================
st.subheader("📌 Umur vs Lokasi Strategik")
grouped = data.groupby(['Umur', 'Lokasi_strategik']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
for col in grouped.columns:
    ax.plot(grouped.index, grouped[col], marker='o', label=col)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Umur vs Lokasi Strategik")
ax.legend(title="Lokasi Strategik")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# ========================
# 3. Keperluan Perpustakaan
# ========================
st.subheader("📌 Umur vs Keperluan Perpustakaan")
grouped = data.groupby(['Umur', 'Keperluan_perpustakaan']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
for col in grouped.columns:
    ax.plot(grouped.index, grouped[col], marker='o', label=col)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Umur vs Keperluan Perpustakaan")
ax.legend(title="Keperluan Perpustakaan")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# ========================
# 4. Kekurangan Pengunjung
# ========================
st.subheader("📌 Umur vs Kekurangan Pengunjung")
grouped = data.groupby(['Umur', 'Kekurangan_pengunjung']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
for col in grouped.columns:
    ax.plot(grouped.index, grouped[col], marker='o', label=col)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Umur vs Kekurangan Pengunjung")
ax.legend(title="Kekurangan Pengunjung")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# ========================
# 5. Operasi Perpustakaan
# ========================
st.subheader("📌 Umur vs Pengoperasian Perpustakaan")
grouped = data.groupby(['Umur', 'Operasi_perpustakaan']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
for col in grouped.columns:
    ax.plot(grouped.index, grouped[col], marker='o', label=col)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Umur vs Pengoperasian Perpustakaan")
ax.legend(title="Operasi Perpustakaan")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# ========================
# 6. Histogram: Jarak Lokasi
# ========================
st.subheader("📌 Histogram: Bilangan Responden vs Jarak Lokasi")
grouped = data.groupby(['Umur', 'Jarak_lokasi']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(6, 4))
grouped.plot(kind='bar', ax=ax, width=0.8)
ax.set_xlabel("Kumpulan Umur")
ax.set_ylabel("Bilangan Responden")
ax.set_title("Histogram: Bilangan Responden vs Jarak Lokasi")
ax.legend(title="Jarak Lokasi")
ax.grid(axis='y', linestyle='--', alpha=0.6)
st.pyplot(fig)
