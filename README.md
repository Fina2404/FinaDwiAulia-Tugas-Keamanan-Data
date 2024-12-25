# Tugas Praktikum Keamanan Data

Repository ini berisi implementasi tiga tugas praktikum terkait Keamanan Data:

1. **Caesar Cipher GUI** (`chipergui.py`)
2. **DES Encryption GUI** (`desgui.py`)
3. **Steganography GUI** (`steganogui.py`)

## Deskripsi Tugas

### 1. Caesar Cipher GUI
- Aplikasi ini mengimplementasikan Caesar Cipher untuk mengenkripsi dan mendekripsi teks.
- Fitur utama:
  - Pilihan jenis alfabet (A-Z atau A-Z dengan angka 0-9).
  - Input nilai pergeseran untuk enkripsi dan dekripsi.
  - Antarmuka pengguna berbasis Streamlit.

### 2. DES Encryption GUI
- Aplikasi ini mengimplementasikan algoritma Data Encryption Standard (DES) untuk enkripsi dan dekripsi.
- Fitur utama:
  - Input teks dan kunci (8 karakter).
  - Enkripsi teks menjadi ciphertext menggunakan mode ECB.
  - Dekripsi ciphertext kembali menjadi plaintext.
  - Antarmuka pengguna berbasis Streamlit.

### 3. Steganography GUI
- Aplikasi ini memungkinkan penyembunyian dan pengungkapan pesan dalam file gambar menggunakan teknik steganografi.
- Fitur utama:
  - Menyembunyikan pesan dalam gambar (format .png atau .jpg).
  - Mengungkap pesan tersembunyi dari gambar.
  - Antarmuka pengguna berbasis Streamlit.

## Cara Menjalankan

### Prasyarat
- Python 3.8 atau lebih baru
- Library yang diperlukan:
  - `streamlit`
  - `streamlit-lottie`
  - `pycryptodome`
  - `stegano`

Instal semua dependensi dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi

1. Clone repository ini:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Jalankan setiap aplikasi sesuai tugas:

   **Caesar Cipher GUI**:
   ```bash
   streamlit run chipergui.py
   ```

   **DES Encryption GUI**:
   ```bash
   streamlit run desgui.py
   ```

   **Steganography GUI**:
   ```bash
   streamlit run steganogui.py
   ```

3. Ikuti petunjuk di antarmuka untuk menggunakan fitur aplikasi.

## Struktur File
```
|-- chipergui.py       # Implementasi Caesar Cipher GUI
|-- desgui.py          # Implementasi DES Encryption GUI
|-- steganogui.py      # Implementasi Steganography GUI
|-- README.md          # Dokumentasi repository
```

## Penulis
Nama: Fina Dwi Aulia  
Mata Kuliah: Keamanan Data
