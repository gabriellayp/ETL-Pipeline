from utils.extract.extract_data import crawl_all_pages
from utils.transform.transform_data import preprocess_data
from utils.load.load_data import save_to_csv

def main():
    print("Memulai proses ETL...")

    raw_data = crawl_all_pages()
    if not raw_data:
        print("Data kosong, ETL dihentikan.")
        return

    clean_data = preprocess_data(raw_data)
    if clean_data.empty:
        print("Data setelah transformasi kosong, ETL dihentikan.")
        return

    save_to_csv(clean_data, "products_cleaned.csv")
    print("ETL selesai.")

if __name__ == "__main__":
    main()