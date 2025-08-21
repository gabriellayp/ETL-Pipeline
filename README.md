# Submission - ETL Pipeline Project

## Cara Menjalankan Skrip ETL Pipeline

1. Buka terminal/command prompt dan masuk ke direktori utama proyek.
2. Jalankan perintah:

   python main.py

3. Jika berhasil, data akan diekstrak dari website, dibersihkan, dan disimpan dalam file bernama `products_clean.csv`.

---

## Cara Menjalankan Unit Test

1. Jalankan perintah berikut untuk mengeksekusi seluruh unit test:

   python -m unittest discover -s tests -v

2. Penjelasan:
   - Semua file di folder `tests/` yang namanya diawali dengan `test_` akan dijalankan.
   - Meliputi pengujian fungsi ekstraksi (`fetch_product_data`), transformasi (`bersihkan_data`), dan penyimpanan (`simpan_ke_csv`).
   - Mocking diterapkan pada fungsi yang melakukan request dan penulisan file agar pengujian tetap stabil tanpa tergantung jaringan atau file system.

---

## Cara Menjalankan Test Coverage

1. Install pustaka `coverage` jika belum terpasang:

   pip install coverage

2. Jalankan perintah ini untuk menjalankan test sambil mengukur coverage:

   coverage run -m unittest discover -s tests

3. Untuk menampilkan hasilnya di terminal:

   coverage report
---

## Struktur Direktori Proyek

```bash
submission/
├── main.py
├── products_clean.csv
├── submission.txt
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
└── utils/
    ├── extract/
    │   └── extract_data.py       # Fungsi `fetch_product_data` untuk ekstraksi data dari web
    ├── transform/
    │   └── transform_data.py     # Fungsi `bersihkan_data` untuk membersihkan dan validasi data
    └── load/
        └── load_data.py          # Fungsi `simpan_ke_csv` untuk menyimpan data ke file CSV
