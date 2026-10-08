# projetcs_python

Python notebooks (Google Colab) organised by project: **Odoo / Teepee** integration, **Cegelec NC** data preparation, **address** cleaning (New Caledonia, French Polynesia) and exercises from the **Data Analyst** training course.

## Organisation

| Folder | Content |
|---|---|
| [`odoo-axians/`](odoo-axians/) | Extraction through the Odoo API (XML-RPC): Helpdesk tickets, users, clients |
| [`migration-odoo-teepee/`](migration-odoo-teepee/) | Preparation of Odoo clients, contacts and tickets before import into Teepee |
| [`teepee/`](teepee/) | Authentication and call tests for the Teepee API |
| [`cegelec-nc/`](cegelec-nc/) | Cleaning of Cegelec New Caledonia client exports, Codex client list |
| [`sites-equipements/`](sites-equipements/) | Sites (FANC) and equipment |
| [`adresses/`](adresses/) | City / district / postal code reference lists (New Caledonia, French Polynesia) |
| [`vin-millesimes/`](vin-millesimes/) | Cleaning of the wine estates, comments and appellations tables |
| [`formation-data-analyst/`](formation-data-analyst/) | Exercises and case studies (Python, pandas, statistics, EDA) |
| [`tools/`](tools/) | Utility scripts (notebook cleaning before commit) |

Each folder has its own `README.md` (purpose, inputs, outputs, execution order).

## Repository rules

1. **No secrets in notebooks.** Credentials are read through `os.environ[...]`; the list of variables is in [`.env.example`](.env.example).
2. **No client data.** `.xlsx` / `.csv` files are ignored (`.gitignore`) and notebooks are versioned **without outputs**.
3. Before committing a new notebook:
   ```bash
   python tools/clean_notebook.py my_notebook.ipynb my_notebook.ipynb
   ```
   The script removes outputs, strips Colab metadata and replaces hard-coded credentials with environment variables.

## Using the notebooks in Colab

Open a notebook from GitHub (`File > Open notebook > GitHub`), then fill in the variables in Colab's **Secrets** panel and expose them with:

```python
import os
from google.colab import userdata
for k in ["ODOO_URL", "ODOO_DB", "ODOO_USERNAME", "ODOO_API_KEY"]:
    os.environ[k] = userdata.get(k)
```

## Local installation

```bash
pip install -r requirements.txt
```
