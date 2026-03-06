import pandas as pd


def fix_veckapris(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    s = df["veckapris"].astype(str).str.lower()
    s = s.str.replace(r"[^0-9,\.]", "", regex=True)
    s = s.str.replace(",", ".", regex=False)
    df["veckapris"] = pd.to_numeric(s, errors="coerce")
    return df


def fix_kasstyp(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    s = df["kasstyp"].astype(str).str.strip().str.lower()

    kasstyp_map = {
        "klassisk": "Klassisk",
        "classic": "Klassisk",
        "familj": "Familj",
        "family": "Familj",
        "vegetarisk": "Vegetarisk",
        "vegetarian": "Vegetarisk",
        "vego": "Vegetarisk",
        "snabb": "Snabb",
        "snabbkasse": "Snabb",
        "premium": "Premium",
    }

    df["kasstyp"] = s.map(kasstyp_map).fillna(s.str.title())
    return df


def fix_kostpreferens(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    s = df["kostpreferens"].astype(str).str.strip().str.lower()

    kost_map = {
        "standard": "Standard",
        "": "Standard",
        "nan": "Standard",
        "laktosfri": "Laktosfri",
        "laktos": "Laktosfri",
        "glutenfri": "Glutenfri",
        "gluten": "Glutenfri",
        "nötfri": "Nötfri",
        "nötter": "Nötfri",
        "fläskfri": "Fläskfri",
        "no pork": "Fläskfri",
        "vegetarisk": "Vegetarisk",
        "vegetarian": "Vegetarisk",
        "vego": "Vegetarisk",
    }

    df["kostpreferens"] = s.map(kost_map).fillna("Standard")
    return df


def fix_dates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    date_cols = [
        "pren_startdatum",
        "paus_från",
        "paus_till",
        "pren_avslutsdatum",
        "leveransdatum",
        "omdömesdatum",
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def transform_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    df_clean = fix_veckapris(df_clean)
    df_clean = fix_kasstyp(df_clean)
    df_clean = fix_kostpreferens(df_clean)
    df_clean = fix_dates(df_clean)
    return df_clean


if __name__ == "__main__":
    df = pd.read_csv("matkassen_data.csv")
    df_clean = transform_pipeline(df)
    df_clean.to_csv("matkassen_cleaned.csv", index=False)
    print("ETL pipeline completed successfully.")