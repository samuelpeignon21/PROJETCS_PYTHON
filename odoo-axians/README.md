# Odoo – Axians NC

Notebooks d'extraction de données depuis l'API Odoo (XML-RPC), utilisées en entrée de Power BI.

| Notebook | Objectif | Sortie |
|---|---|---|
| `test_connexion_api_odoo_pbi.ipynb` | Teste la connexion, puis extrait les tickets `helpdesk.ticket` par pages de 100 (tri sur `id` pour éviter une boucle infinie), les utilisateurs `res.users` et les clients `res.partner` | `tickets.xlsx` |

## Variables d'environnement

`ODOO_URL`, `ODOO_DB`, `ODOO_USERNAME`, `ODOO_API_KEY` (voir `../.env.example`).

> Au dernier passage : 11 404 tickets, 43 agents, environ 1 900 clients distincts.
