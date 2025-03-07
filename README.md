# Proyek-Akhir-Analisis-Data

## Menjalankan Analisis Data di Google Colab
1. Pastikan Anda telah mengunduh proyek ini ke perangkat Anda.
2. Klik File > New Notebook untuk membuat notebook baru.
3. Pilih file dengan ekstensi .ipynb yang telah diunduh.
4. Klik Connect untuk menyambungkan ke hosted runtime.
5. Eksekusi setiap sel kode untuk memproses analisis data.
   
## Menjalankan Dashboard
Mengunduh proyek ini. Sebelum menjalankan aplikasi Streamlit, Anda perlu mengatur lingkungan pengembangan terlebih dahulu. Berikut adalah dua metode yang bisa digunakan: menggunakan Anaconda atau terminal biasa.

## Setup Environment - Anaconda
Jika menggunakan Anaconda, ikuti langkah-langkah berikut:
1. Gunakan Python 3.9 atau yang lebih baru

   ```conda create --name main-ds python=3.9```
   
3. Aktifkan lingkungan virtual yang telah dibuat

   ```conda activate main-ds```
   
5. Instal semua dependensi yang diperlukan

   ```pip install -r requirements.txt```

## Setup Environment - Shell/Terminal
Jika tidak menggunakan Anaconda, Anda dapat mengelola lingkungan menggunakan pipenv
1. Buat direktori baru untuk proyek
  
   ```mkdir proyek_analisis_data```
   
2. Masuk ke direktori proyek

   ```cd proyek_analisis_data```

3. Install dan inisialisasi pipenv

   ```pipenv install```
   
5. Aktifkan lingkungan pipenv

   ```pipenv shell```

6. Instal semua dependensi yang dibutuhkan

   ```pip install -r requirements.txt```

## Menjalankan Aplikasi Streamlit
Setelah lingkungan siap dan semua dependensi telah diinstal, jalankan aplikasi dengan perintah

```streamlit run dashboard.py``` atau ```python -m streamlit run dashboard/dashboard.py```

Perintah ini akan membuka aplikasi di browser web anda dan berinteraksi dengan dashboard yang telah dibuat.

Jika ada pertanyaan terkait proyek ini, hubungi: firdahumaira13@gmail.com

© 2025 Firda Humaira
