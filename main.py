import streamlit as st

st.set_page_config(page_title="Kajian Perpustakaan", layout="wide")

# --- Navigation ---
st.sidebar.title("📂 Pilih Kawasan")
page = st.sidebar.selectbox("Navigasi", ["Bukit Merah", "Desa Sempeneh", "Kuala Dipang"])

# --- Bukit Merah Page ---
if page == "Bukit Merah":
    st.title("📚 Analisis Penutupan Perpustakaan Bukit Merah")

# --- Desa Sempeneh Page ---
elif page == "Desa Sempeneh":
    st.title("📖 Analisis Perpustakaan Desa Sempeneh")

# --- Kuala Dipang Page ---
elif page == "Kuala Dipang":
    st.title("📖 Analisis Perpustakaan Desa Sempeneh")
