# Migration Odoo → Teepee

Préparation des données Odoo (Axians NC) avant import dans Teepee. Chaque notebook part d'un export Excel d'Odoo (non versionné) et produit un fichier prêt à importer.

Ordre conseillé : **clients → entreprise principale associée → contacts → tickets**.

| Notebook | Objectif |
|---|---|
| `odoo_clients_axians` | Sociétés, équipements et étiquettes : nettoyage des valeurs, normalisation des villes et pays, séparation société / équipements |
| `entreprise_principale_associee_odoo_axians` | Rattache chaque site à son entreprise principale à partir du mapping sites ↔ entreprises et de l'export Teepee des sites |
| `odoo_contacts_axians` | Contacts : noms, courriels (`Nom <mail>` → mail seul), postes et titres ; suppression des lignes parasites |
| `ticket_odoo_vers_teepee` | Tickets Helpdesk : nettoyage du HTML des messages, regroupement des échanges dans une description complète, export `tickets_odoo_nettoyes.xlsx` |

Dépendances supplémentaires : `rapidfuzz`, `unidecode`.
