# Yield Predictor Benin

Prediction et aide a la decision pour les rendements agricoles au Benin.
Premiere culture : mais (departement, saison principale). Pipeline pense pour
etre reutilise avec d'autres cultures (riz, manioc, igname...) via `config/<culture>.yaml`.

## Demarrage
Lancer les commandes **une par une** :

```
python -m venv .venv
```
Activer l'environnement :
- Windows PowerShell : `.venv\Scripts\Activate.ps1`
- Windows cmd : `.venv\Scripts\activate.bat`
- Mac / Linux : `source .venv/bin/activate`

```
pip install -r requirements.txt
python -m pytest
jupyter lab
```
1. Telecharger les rendements (ex. FEWS NET Data Explorer) dans `data/raw/`.
2. Adapter `config/maize.yaml` (nom du fichier, noms de colonnes).
3. (Fichier utilise : export FEWS NET JSON, commune, 2000-2023.)
4. Ouvrir `notebooks/01_audit_rendements.ipynb`.

## Sources de donnees (a completer avec la date de telechargement)
| Donnee | Source | Telecharge le |
|---|---|---|
| Rendements | | |
| Pluie | CHIRPS | |
| Temperature | ERA5 / NASA POWER | |
| Vegetation | MODIS / Sentinel-2 (NDVI) | |
| Sol | SoilGrids | |

## Regles
- Ne jamais modifier `data/raw/`.
- Evaluer par annee (leave-one-year-out), jamais par tirage aleatoire.
- Toujours comparer a un modele de reference (moyenne / tendance).
