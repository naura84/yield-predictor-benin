import json
import src.data.load_yields as ly


def test_load_json_filters_and_year(tmp_path, monkeypatch):
    rows = [
        {"admin_2": "A", "season_year": "Main 2000", "value": 1.0,
         "product": "Maize (Corn)", "indicator": "Yield", "season_name": "Main"},
        {"admin_2": "A", "season_year": "Main 2001", "value": None,
         "product": "Maize (Corn)", "indicator": "Yield", "season_name": "Main"},
        {"admin_2": "A", "season_year": "Main 2000", "value": 9.0,
         "product": "Sorghum", "indicator": "Yield", "season_name": "Main"},
    ]
    (tmp_path / "data" / "raw").mkdir(parents=True)
    (tmp_path / "data" / "raw" / "t.json").write_text(json.dumps(rows))
    monkeypatch.setattr(ly, "ROOT", tmp_path)

    cfg = {"years": [2000, 2023], "yields": {
        "file": "t.json", "format": "json",
        "filters": {"product": "Maize (Corn)", "indicator": "Yield", "season_name": "Main"},
        "columns": {"admin": "admin_2", "year": "season_year", "value": "value"},
        "year_regex": r"(\d{4})"}}
    df = ly.load_yields(cfg)
    assert len(df) == 2                     # sorgho exclu
    assert df["value"].isna().sum() == 1    # manquant conserve, pas transforme en 0
    assert sorted(df["year"]) == [2000, 2001]
