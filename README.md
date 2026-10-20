# Secure Text Analyzer & DevSecOps Pipeline

## 1. Nama Aplikasi & Fungsi
Aplikasi ini adalah **Secure Text Analyzer**, sebuah utilitas berbasis Python yang berfungsi untuk membersihkan input teks dari potensi kerentanan injeksi (seperti XSS dasar) serta melakukan analisis statistik teks secara aman.

## 2. Bahasa & Framework
* **Bahasa Pemrograman:** Python 3.10
* **Testing Framework:** Pytest
* **Security Scanner (SAST):** Bandit

## 3. Cara Menjalankan Aplikasi
1. Install dependencies:
   `pip install -r requirements.txt`
2. Jalankan unit test:
   `pytest`
3. Jalankan aplikasi utama:
   `python src/main.py`

## 4. Overview Pipeline CI/CD DevSecOps
Pipeline ini diotomatisasi menggunakan **GitHub Actions** dengan pemicu `push` dan `pull_request` ke branch `main`. Terdiri dari 2 job utama:
* **Job Build (`build`)**: Menginstal dependensi dan menjalankan unit test otomatis menggunakan `pytest` untuk memastikan fungsionalitas kode berjalan baik.
* **Job SAST Scan (`sast-scan`)**: Bergantung pada job `build`, job ini menjalankan Static Application Security Testing menggunakan **Bandit** untuk mendeteksi celah keamanan pada kode sumber.