import streamlit as st
from stegano import lsb
import os

# Fungsi untuk menyembunyikan pesan
def hide_message(img_path, message, save_path):
    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        return f"Pesan berhasil disembunyikan! Gambar disimpan di: {save_path}"
    except Exception as e:
        return f"Gagal menyembunyikan pesan: {e}"

# Fungsi untuk menampilkan pesan tersembunyi
def reveal_message(img_path):
    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            return f"Pesan tersembunyi: {clear_message}"
        else:
            return "Tidak ada pesan tersembunyi dalam gambar ini."
    except Exception as e:
        return f"Gagal menampilkan pesan: {e}"

# Konfigurasi Streamlit
st.set_page_config(page_title="Steganography Tool", page_icon="📷")

st.markdown("<h1 style='text-align: center; color: #00796B;'>Steganography Tool</h1>", unsafe_allow_html=True)

# Menu Utama
menu = st.sidebar.selectbox("Menu", ["Sembunyikan Pesan", "Tampilkan Pesan"])

if menu == "Sembunyikan Pesan":
    st.subheader("Sembunyikan Pesan dalam Gambar")
    
    # Input file gambar
    uploaded_file = st.file_uploader("Upload gambar (format: .png, .jpg)", type=["png", "jpg"])
    
    if uploaded_file:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        message = st.text_area("Masukkan pesan yang akan disembunyikan")
        save_path = st.text_input("Masukkan path untuk menyimpan gambar dengan pesan tersembunyi (contoh: hidden_image.png)")
        
        if st.button("Sembunyikan Pesan"):
            if save_path:
                result = hide_message(temp_path, message, save_path)
                st.success(result)
                os.remove(temp_path)
            else:
                st.error("Path untuk menyimpan gambar harus diisi.")

elif menu == "Tampilkan Pesan":
    st.subheader("Tampilkan Pesan Tersembunyi dari Gambar")
    
    # Input file gambar
    uploaded_file = st.file_uploader("Upload gambar dengan pesan tersembunyi (format: .png, .jpg)", type=["png", "jpg"])
    
    if uploaded_file:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Tampilkan Pesan"):
            result = reveal_message(temp_path)
            st.success(result)
            os.remove(temp_path)

# Watermark
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; color: #004D40;'>Created by Your Name</div>
    """,
    unsafe_allow_html=True
)
