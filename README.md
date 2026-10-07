# projetcs_python

Notebooks Python (Google Colab) classés par projet : intégration **Odoo / Teepee**, préparation des données **Cegelec NC**, nettoyage d'**adresses** (Nouvelle-Calédonie, Polynésie française) et exercices de la formation **Data Analyst**.

## Organisation

| Dossier | Contenu |
|---|---|
| [`odoo-axians/`](odoo-axians/) | Extraction via l'API Odoo (XML-RPC) : tickets Helpdesk, utilisateurs, clients, contacts |
| [`teepee/`](teepee/) | Tests d'authentification et d'appel de l'API Teepee |
| [`cegelec-nc/`](cegelec-nc/) | Nettoyage des exports clients Cegelec Nouvelle-Calédonie avant import |
| [`adresses/`](adresses/) | Référentiels villes / quartiers / codes postaux (Nouvelle-Calédonie, Polynésie française) |
| `formation-data-analyst/` | Exercices et cas pratiques (Python, pandas, statistiques, EDA) |
| [`tools/`](tools/) | Scripts utilitaires (nettoyage des notebooks avant commit) |

Chaque dossier a son propre `README.md` (objectif, entrées, sorties, ordre d'exécution).

## Règles du dépôt

1. **Aucun secret dans les notebooks.** Les identifiants sont lus via `os.environ[...]` ; la liste des variables est dans [`.env.example`](.env.example).
2. **Aucune donnée client.** Les fichiers `.xlsx` / `.csv` sont ignorés (`.gitignore`) et les notebooks sont versionnés **sans sorties**.
3. Avant de committer un nouveau notebook :
   ```bash
   python tools/clean_notebook.py mon_notebook.ipynb mon_notebook.ipynb
   ```
   Le script supprime les sorties, retire les métadonnées Colab et remplace les identifiants écrits en dur par des variables d'environnement.

## Utilisation dans Colab

Ouvrir un notebook depuis GitHub (`Fichier > Ouvrir le notebook > GitHub`), puis renseigner les variables dans le panneau **Secrets** de Colab et les exposer avec :

```python
import os
from google.colab import userdata
for k in ["ODOO_URL", "ODOO_DB", "ODOO_USERNAME", "ODOO_API_KEY"]:
    os.environ[k] = userdata.get(k)
```

## Installation locale

```bash
pip install -r requirements.txt
```
