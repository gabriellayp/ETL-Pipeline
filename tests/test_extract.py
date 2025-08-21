import unittest
from unittest.mock import patch
import requests
from utils.extract.extract_data import fetch_product_data
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

class TestExtract(unittest.TestCase):

    @patch("utils.extract.extract_data.requests.get")
    def test_fetch_product_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = """
            <div class="collection-card">
                <h3 class="product-title">Test Product</h3>
                <span class="price">$25</span>
                <p>Rating: 4.7 ⭐</p>
                <p>Colors: 5 options</p>
                <p>Size: L</p>
                <p>Gender: Female</p>
            </div>
        """

        result = fetch_product_data("https://test-url.com")
        self.assertEqual(len(result), 1)

        expected = {
            "title": "Test Product",
            "price": "25",
            "rating": "4.7",
            "colors": "5",
            "size": "L",
            "gender": "Female",
        }

        for key in expected:
            self.assertEqual(result[0][key], expected[key])

    @patch("utils.extract.extract_data.requests.get")
    def test_fetch_product_data_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")
        result = fetch_product_data("https://invalid-url.com")
        self.assertEqual(result, [])

    @patch("utils.extract.extract_data.requests.get")
    def test_fetch_product_data_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout("Timeout error")
        result = fetch_product_data("https://timeout-url.com")
        self.assertEqual(result, [])

    @patch("utils.extract.extract_data.requests.get")
    def test_fetch_product_data_empty_page(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<div>No product here</div>"
        result = fetch_product_data("https://empty.com")
        self.assertEqual(result, [])

    @patch("utils.extract.extract_data.requests.get")
    def test_fetch_product_data_missing_fields(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = """
            <div class="collection-card">
                <h3 class="product-title">Incomplete</h3>
            </div>
        """
        result = fetch_product_data("https://incomplete.com")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Incomplete")
        self.assertEqual(result[0]["price"], "")
        self.assertEqual(result[0]["rating"], "")
        self.assertEqual(result[0]["colors"], "")
        self.assertEqual(result[0]["size"], "")
        self.assertEqual(result[0]["gender"], "")

if __name__ == "__main__":
    unittest.main()