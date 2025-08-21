import pandas as pd

def save_to_csv(dataframe, output_file="products.csv"):
    if dataframe.empty:
        print("Data kosong. Tidak disimpan.")
        return

    try:
        dataframe.to_csv(output_file, index=False)
        print(f"Data disimpan ke: {output_file}")
    except Exception as err:
        print(f"Gagal menyimpan file: {err}")
        raise