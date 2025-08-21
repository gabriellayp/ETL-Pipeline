import pandas as pd

RUPIAH_RATE = 16000

def preprocess_data(raw_data):
    if not raw_data:
        return pd.DataFrame()

    try:
        df = pd.DataFrame(raw_data).copy()

        # Validasi kolom
        expected = {"price", "rating", "colors"}
        if not expected.issubset(df.columns):
            print(f"Kolom hilang: {expected - set(df.columns)}")

        # Konversi dan bersih-bersih
        df["price"] = pd.to_numeric(df["price"], errors="coerce") * RUPIAH_RATE
        df["rating"] = df["rating"].astype(str).str.extract(r"([\d.]+)").astype(float)
        df["colors"] = pd.to_numeric(df["colors"], errors="coerce").fillna(0).astype(int)

        df.dropna(subset=["rating", "price"], inplace=True)
        df.drop_duplicates(inplace=True)
        df = df[df["title"] != "Unknown Product"]

        return df

    except Exception as err:
        print(f"Transformasi gagal: {err}")
        return pd.DataFrame()