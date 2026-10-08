# Odoo – Axians NC

Notebooks extracting data from the Odoo API (XML-RPC), used as input for Power BI.

| Notebook | Purpose | Output |
|---|---|---|
| `test_connexion_api_odoo_pbi.ipynb` | Tests the connection, then extracts `helpdesk.ticket` tickets in pages of 100 (sorted on `id` to avoid an infinite loop), `res.users` users and `res.partner` clients | `tickets.xlsx` |

## Environment variables

`ODOO_URL`, `ODOO_DB`, `ODOO_USERNAME`, `ODOO_API_KEY` (see `../.env.example`).

> At the last run: 11,404 tickets, 43 agents, about 1,900 distinct clients.
