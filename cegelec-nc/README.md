# Cegelec Nouvelle-Calédonie

| Notebook | Objectif | Entrée | Sortie |
|---|---|---|---|
| `clients_cegelec_nc.ipynb` | Nettoie l'export Teepee « Entreprise » : renomme les colonnes, regroupe les e-mails (`Mails`) et contacts (`Contacts`) sur plusieurs lignes, remplace les 0 par des vides, normalise villes et pays, complète les adresses de facturation | `TEEPEE_Entreprise_dataExport (3).xlsx` (non versionné) | `df2_export.xlsx` |
| `liste_client_codex.ipynb` | Rapproche la liste clients Codex (`F561_Liste clients ….xlsx`) des entreprises Teepee par comparaison floue de noms (`rapidfuzz`) | Liste clients Codex (non versionnée) | tableau de correspondance |
| `entreprises_bi_planning.ipynb` | Compare les entreprises du planning (statut « Terminé ») avec l'export Teepee « Entreprise » et la liste « Entreprise à prendre » | exports Teepee (non versionnés) | liste d'entreprises à traiter |

Dépendance supplémentaire : `rapidfuzz`.
