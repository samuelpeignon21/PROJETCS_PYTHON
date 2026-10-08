# Cegelec New Caledonia

| Notebook | Purpose | Input | Output |
|---|---|---|---|
| `clients_cegelec_nc.ipynb` | Cleans the Teepee "Entreprise" export: renames columns, groups e-mails (`Mails`) and contacts (`Contacts`) spread over several rows, replaces 0 with blanks, normalises cities and countries, completes billing addresses | `TEEPEE_Entreprise_dataExport (3).xlsx` (not versioned) | `df2_export.xlsx` |
| `liste_client_codex.ipynb` | Matches the Codex client list (`F561_Liste clients ….xlsx`) against Teepee companies using fuzzy name comparison (`rapidfuzz`) | Codex client list (not versioned) | matching table |
| `entreprises_bi_planning.ipynb` | Compares the companies of the planning ("Terminé" / done status) with the Teepee "Entreprise" export and the "Entreprise à prendre" (companies to handle) list | Teepee exports (not versioned) | list of companies to process |

Additional dependency: `rapidfuzz`.
