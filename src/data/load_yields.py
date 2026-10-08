import json
import pandas as pd
from src.config import ROOT


def load_yields(cfg: dict) -> pd.DataFrame:
    """Charge les rendements bruts et renvoie un tableau propre :
    colonnes admin, year, value. Aucune ecriture dans data/raw."""
    ycfg = cfg["yields"]
    path = ROOT / "data" / "raw" / ycfg["file"]

    if ycfg.get("format", "csv") == "json":
        with open(path, encoding="utf-8") as f:
            df = pd.DataFrame(json.load(f))
    else:
        df = pd.read_csv(path, na_values=ycfg.get("missing_values", []))

    # 1. Filtres (culture, indicateur, saison...)
    for col, expected in ycfg.get("filters", {}).items():
        df = df[df[col] == expected]

    # 2. Renommage des colonnes
    cols = ycfg["columns"]
    df = df.rename(columns={v: k for k, v in cols.items()})

    # 3. Annee : extraite par regex si la colonne est du texte ("Main 2023")
    regex = ycfg.get("year_regex")
    if regex:
        df["year"] = df["year"].astype(str).str.extract(regex)[0]
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df = df.dropna(subset=["year"])
    df["year"] = df["year"].astype(int)

    # 4. Periode demandee
    y0, y1 = cfg["years"]
    df = df[(df["year"] >= y0) & (df["year"] <= y1)].copy()

    # 5. Valeurs : vide = manquant (jamais zero)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df[["admin", "year", "value"]].reset_index(drop=True)
