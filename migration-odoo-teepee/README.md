# Odoo → Teepee migration

Preparation of Odoo data (Axians NC) before import into Teepee. Each notebook starts from an Odoo Excel export (not versioned) and produces a file ready to import.

Recommended order: **clients → associated main company → contacts → tickets**.

| Notebook | Purpose |
|---|---|
| `odoo_clients_axians` | Companies, equipment and tags: value cleaning, city and country normalisation, separation of company / equipment |
| `entreprise_principale_associee_odoo_axians` | Links each site to its main company using the sites ↔ companies mapping and the Teepee sites export |
| `odoo_contacts_axians` | Contacts: names, e-mails (`Name <mail>` → mail only), positions and titles; removal of stray rows |
| `ticket_odoo_vers_teepee` | Helpdesk tickets: cleaning of message HTML, grouping of exchanges into a complete description, export of `tickets_odoo_nettoyes.xlsx` |

Additional dependencies: `rapidfuzz`, `unidecode`.
