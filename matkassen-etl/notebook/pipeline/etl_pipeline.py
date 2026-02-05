import pandas as pd


def clean_week_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Städar veckapris: klarar '499 kr', '499SEK', '499:-', komma/punkt m.m.
    """
    s = df["veckapris"].astype(str).str.lower()

    s = s.str.replace(",", ".", regex=False)
    s = (
        s.str.replace("sek", "", regex=False)
         .str.replace("kr", "", regex=False)
         .str.replace(":-", "", regex=False)
         .str.replace(" ", "", regex=False)
    )

    # plockar första talet som finns
    s = s.str.extract(r"(\d+(?:\.\d+)?)", expand=False)

    df["veckapris"] = pd.to_numeric(s, errors="coerce")
    return df



def normalize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliserar kasstyp så samma kategori inte finns i flera varianter
    """
    df["kasstyp"] = df["kasstyp"].replace({
        "Classic": "Klassisk",
        "KLASSISK": "Klassisk",
        "klassisk": "Klassisk",
        "Family": "Familj",
        "FAMILJ": "Familj",
        "familj": "Familj",
        "VEGETARISK": "Vegetarisk",
        "vegetarisk": "Vegetarisk",
        "Veg": "Vegetarisk"
    })
    return df


def clean_delivery_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliserar leveransstatus till Levererad / Missad
    """
    df["leveransstatus"] = df["leveransstatus"].replace({
        "Delivered": "Levererad",
        "Ok": "Levererad",
        "missad": "Missad"
    })
    return df


def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Konverterar datumkolumner till datetime
    """
    date_cols = [
        "pren_startdatum",
        "paus_från",
        "paus_till",
        "pren_avslutsdatum",
        "leveransdatum",
        "omdömesdatum"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Huvudfunktion som kör hela ETL-pipelinen
    """
    df = clean_week_price(df)
    df = normalize_categories(df)
    df = clean_delivery_status(df)
    df = parse_dates(df)
    return df
if __name__ == "__main__":
    print("ETL pipeline startar 🚀")

    df_raw = pd.read_csv(
        "matkassen-etl/notebook/matkassen_data.csv"
    )

    print("Rådata inläst:", df_raw.shape)

    df_clean = run_pipeline(df_raw)

    print("Data efter pipeline:", df_clean.shape)

    df_clean.to_csv(
        "matkassen-etl/notebook/matkassen_data_clean.csv",
        index=False
    )

    print("Tvättad data sparad ✅")