# Address reference lists

Preparation of **City / District / Postal code** lists to import into the target tool.

| Notebook | Territory | Input (not versioned) | Outputs |
|---|---|---|---|
| `nc_adresses.ipynb` | New Caledonia | `Adresses_Nouvelle_Caledonie.xlsx` | postal codes per municipality (`postal_map`), `df2_export.xlsx`, lists `V_NC.xlsx`, `Q_NC.xlsx`, `C_NC.xlsx` |
| `polynesie_francaise_adresses.ipynb` | French Polynesia | `districts2017.csv` (`;` separator, latin1) | postal codes per municipality, `df3_export.xlsx`, `df3V/Q/CP_export.xlsx` |

Common principle: load the source file, associate a postal code with each municipality through a dictionary, then export the de-duplicated lists (cities, districts, postal codes).
