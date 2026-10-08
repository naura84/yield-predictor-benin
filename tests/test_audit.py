import pandas as pd
from src.data.audit import yield_matrix, missing_report


def test_matrix_and_report():
    df = pd.DataFrame({
        "admin": ["A", "A", "B"],
        "year": [2000, 2001, 2000],
        "value": [1.0, 1.2, 0.9],
    })
    m = yield_matrix(df)
    assert m.shape == (2, 2)
    rep = missing_report(m)
    assert rep["cellules_renseignees"] == 3
    assert rep["taux_remplissage"] == 0.75
