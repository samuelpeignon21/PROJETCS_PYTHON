# Wines and vintages

Cleaning of the tables of a project about wine estates, vintages and appellations. The source files (`Principal_Domaines.xlsx`, `Principal_Commentaires.xlsx`, `Lien_Appelation_Region.csv`) are not versioned.

| Notebook | Table processed | Main steps |
|---|---|---|
| `notebook_domaines` | Estates (*Domaines*) | text fixing (`ftfy`), replacement of fake NaNs, extraction of the domain from URLs |
| `notebook_commentaires` | Comments | same, plus column selection and typing, null-value rate |
| `notebook_app_region` | Appellation / region link | cleaning of the mapping table |

Additional dependency: `ftfy` (`pip install ftfy`).
