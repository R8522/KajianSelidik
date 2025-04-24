import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Analisis Perpustakaan", layout="wide")
st.title("📚 Sistem Analisis Perpustakaan Desa/Komuniti")

# Sidebar Navigation
st.sidebar.header("📂 Pilih Lokasi")
page = st.sidebar.selectbox(
    "Lokasi Komuniti:",
    ["Desa Sempeneh", "Bukit Merah"]
)

# Routing
if page == "Desa Sempeneh":
    import DesaSempeneh
    DesaSempeneh.run()

elif page == "Bukit Merah":
    import BukitMerah
    BukitMerah.run()
