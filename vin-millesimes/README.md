# Vins et millésimes

Nettoyage des tables d'un projet sur les domaines viticoles, les millésimes et les appellations. Les fichiers sources (`Principal_Domaines.xlsx`, `Principal_Commentaires.xlsx`, `Lien_Appelation_Region.csv`) ne sont pas versionnés.

| Notebook | Table traitée | Principales étapes |
|---|---|---|
| `notebook_domaines` | Domaines | correction des textes (`ftfy`), remplacement des faux NaN, extraction du domaine des URL |
| `notebook_commentaires` | Commentaires | idem, sélection et typage des colonnes, taux de valeurs nulles |
| `notebook_app_region` | Lien appellation / région | nettoyage de la table de correspondance |

Dépendance supplémentaire : `ftfy` (`pip install ftfy`).
