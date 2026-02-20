nano matkassen-etl/notebook/pipeline/etl_pipeline.pyimport pandas as pd


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


def transform_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    df_clean = fix_veckapris(df_clean)
    df_clean = fix_kasstyp(df_clean)
    df_clean = fix_kostpreferens(df_clean)
    return df_clean
