# Référentiels d'adresses

Préparation des listes **Ville / Quartier / Code postal** à importer dans l'outil cible.

| Notebook | Territoire | Entrée (non versionnée) | Sorties |
|---|---|---|---|
| `nc_adresses.ipynb` | Nouvelle-Calédonie | `Adresses_Nouvelle_Caledonie.xlsx` | codes postaux par commune (`postal_map`), `df2_export.xlsx`, listes `V_NC.xlsx`, `Q_NC.xlsx`, `C_NC.xlsx` |
| `polynesie_francaise_adresses.ipynb` | Polynésie française | `districts2017.csv` (séparateur `;`, latin1) | codes postaux par commune, `df3_export.xlsx`, `df3V/Q/CP_export.xlsx` |

Principe commun : charger le fichier source, associer un code postal à chaque commune via un dictionnaire, puis exporter les listes dédupliquées (villes, quartiers, codes postaux).
