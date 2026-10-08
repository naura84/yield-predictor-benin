from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_config(crop: str) -> dict:
    """Charge config/<crop>.yaml (ex. load_config('maize'))."""
    path = ROOT / "config" / f"{crop}.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)
