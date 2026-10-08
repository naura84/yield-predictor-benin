import pandas as pd


def yield_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Tableau departements x annees (NaN = donnee manquante)."""
    return df.pivot_table(index="admin", columns="year", values="value", aggfunc="mean")


def missing_report(matrix: pd.DataFrame) -> dict:
    total = matrix.size
    present = int(matrix.notna().sum().sum())
    return {
        "zones": matrix.shape[0],
        "annees": matrix.shape[1],
        "cellules_possibles": total,
        "cellules_renseignees": present,
        "taux_remplissage": round(present / total, 3) if total else 0.0,
    }


def flag_outliers(df: pd.DataFrame, z: float = 3.0) -> pd.DataFrame:
    """Valeurs a zero ou tres eloignees de la moyenne du departement."""
    g = df.groupby("admin")["value"]
    zscore = (df["value"] - g.transform("mean")) / g.transform("std")
    return df[(df["value"] == 0) | (zscore.abs() > z)]
