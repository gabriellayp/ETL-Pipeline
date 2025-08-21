import unittest
import pandas as pd
import os
from utils.load.load_data import save_to_csv  # Pastikan path-nya sesuai struktur direktori proyekmu

class SimpanDataTestCase(unittest.TestCase):

    def setUp(self):
        # Nama file dummy untuk testing
        self.test_file = "dummy_output.csv"

    def tearDown(self):
        # Menghapus file jika sudah dibuat
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_menyimpan_dataframe_valid(self):
        # Buat DataFrame contoh
        data = {
            "Title": ["Produk A"],
            "Price": [100000],
            "Rating": [4.5],
            "Colors": [2],
            "Size": ["M"],
            "Gender": ["Unisex"]
        }
        df = pd.DataFrame(data)

        # Simpan ke file
        save_to_csv(df, self.test_file)

        # Cek apakah file benar-benar tersimpan
        self.assertTrue(os.path.exists(self.test_file))

        # Baca ulang dan cocokkan
        loaded_df = pd.read_csv(self.test_file)
        pd.testing.assert_frame_equal(df, loaded_df)

    def test_tidak_menyimpan_jika_dataframe_kosong(self):
        df_kosong = pd.DataFrame()
        save_to_csv(df_kosong, self.test_file)
        self.assertFalse(os.path.exists(self.test_file))  # File tidak seharusnya dibuat

    def test_penanganan_error_pada_simpan(self):
        df = pd.DataFrame({"Title": ["Contoh"], "Price": [12345]})
        # Tes dengan nama file yang tidak valid (folder yang tidak ada)
        with self.assertRaises(Exception):
            save_to_csv(df, "/folder/tidak/ada/output.csv")

if __name__ == "__main__":
    unittest.main()