import unittest
import pandas as pd
from utils.transform.transform_data import preprocess_data

class TransformDataTestCase(unittest.TestCase):

    def test_data_tersaring_dengan_baik(self):
        input_data = [
            {"title": "Kaos A", "price": "12", "rating": "4.2", "colors": "5", "size": "M", "gender": "Pria"},
            {"title": "Kaos B", "price": "20", "rating": "4.7", "colors": "3", "size": "L", "gender": "Wanita"},
        ]
        hasil = preprocess_data(input_data)

        self.assertEqual(len(hasil), 2)
        self.assertTrue(all(hasil["price"] == pd.Series([192000, 320000])))
        self.assertTrue(all(hasil["rating"] == pd.Series([4.2, 4.7])))

    def test_jika_data_tidak_valid_dihapus(self):
        input_data = [
            {"title": "Produk Rusak", "price": "N/A", "rating": "Invalid", "colors": "abc"}
        ]
        hasil = preprocess_data(input_data)
        self.assertEqual(len(hasil), 0)

    def test_hanya_baris_valid_yang_diproses(self):
        input_data = [
            {"title": "Produk A", "price": "25", "rating": "4.5", "colors": "2", "size": "M", "gender": "Unisex"},
            {"title": "Produk B", "price": "N/A", "rating": "None", "colors": "x"},
        ]
        hasil = preprocess_data(input_data)
        self.assertEqual(len(hasil), 1)
        self.assertIn("Produk A", hasil["title"].values)

    def test_harga_tak_valid_dibuang(self):
        input_data = [
            {"title": "Barang X", "price": "tidak_ada", "rating": "4.0", "colors": "2"}
        ]
        hasil = preprocess_data(input_data)
        self.assertEqual(len(hasil), 0)

    def test_kosongkan_dataframe_dari_input_kosong(self):
        hasil = preprocess_data([])
        self.assertTrue(isinstance(hasil, pd.DataFrame))
        self.assertTrue(hasil.empty)

    def test_input_none_dihandle_dengan_aman(self):
        hasil = preprocess_data(None)
        self.assertTrue(isinstance(hasil, pd.DataFrame))
        self.assertTrue(hasil.empty)

if __name__ == "__main__":
    unittest.main()