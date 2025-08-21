import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

USER_AGENT = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/96.0.4664.110 Safari/537.36"
    )
}

ROOT_URL = "https://fashion-studio.dicoding.dev/"
TOTAL_PAGES = 50
MAX_ITEMS = 1000

def fetch_product_data(page_url: str) -> list:
    try:
        res = requests.get(page_url, headers=USER_AGENT, timeout=10)
        res.raise_for_status()
    except Exception as error:
        print(f"Gagal mengambil data dari {page_url}: {error}")
        return []

    parser = BeautifulSoup(res.text, "html.parser")
    product_cards = parser.find_all("div", class_="collection-card")
    collected_data = []

    for card in product_cards:
        name = card.find("h3", class_="product-title")
        price = card.find("span", class_="price")
        rating_info = card.find("p", string=lambda txt: txt and "Rating" in txt)
        color_info = card.find("p", string=lambda txt: txt and "Colors" in txt)
        size_info = card.find("p", string=lambda txt: txt and "Size" in txt)
        gender_info = card.find("p", string=lambda txt: txt and "Gender" in txt)

        record = {
            "title": name.text.strip() if name else "Unknown Product",
            "price": price.text.strip().replace("$", "") if price else "",
            "rating": rating_info.text.replace("Rating:", "").replace("⭐", "").strip() if rating_info else "",
            "colors": color_info.text.replace("Colors:", "").strip().split()[0] if color_info else "",
            "size": size_info.text.replace("Size:", "").strip() if size_info else "",
            "gender": gender_info.text.replace("Gender:", "").strip() if gender_info else "",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(record)

    return collected_data

def crawl_all_pages():
    results = []

    for i in range(1, TOTAL_PAGES + 1):
        if len(results) >= MAX_ITEMS:
            break
        try:
            target_url = ROOT_URL if i == 1 else f"{ROOT_URL}page{i}"
            print(f"Memproses: {target_url}")
            items = fetch_product_data(target_url)
            results.extend(items)
            if len(results) >= MAX_ITEMS:
                break
            time.sleep(1)
        except Exception as err:
            print(f"Terjadi kendala saat mengakses halaman {i}: {err}")
    
    results = results[:MAX_ITEMS]
    print(f"\nTotal produk terkumpul: {len(results)}")
    return results