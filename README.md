# Pousse — interface Ferixu

Début de l’interface NiceGUI du projet Ferixu, inspiré des maquettes du dépôt backend. Les trois pages présentent des **données fictives**. L’interface ne communique pas encore avec le backend, MQTT ou le matériel; les paramètres et commandes sont désactivés.

## Démarrage

Avec Python 3.10 ou plus récent :

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Ouvrir http://localhost:8080. Pour arrêter le serveur, utiliser Ctrl+C.

## Organisation

- `main.py` : enregistrement des pages et lancement.
- `layout.py` : navigation et mise en page communes.
- `pages/` : une page par route (`/`, `/historique`, `/parametres`).
- `composants/` : éléments d’interface réutilisables.
- `models/` : structures et données d’exemple, séparées de l’affichage.
- `assets/` : styles de la maquette.

Cette structure suit les [notes du cours](https://cours-5.gitbook.io/420-5p0-integration-dobjets-connectes/app-client-nicegui/structure-du-projet) et l’exemple [Le nid familial](https://github.com/5P0-Integration-d-objets-connectes/le-nid-familial). Les graphiques utilisent `ui.echart`, comme dans les [notes sur les graphiques](https://cours-5.gitbook.io/420-5p0-integration-dobjets-connectes/app-client-nicegui/graphiques-et-autre). Le point d’entrée et la version de NiceGUI s’inspirent aussi de [demo-nicegui-app-form-valid](https://github.com/5P0-Integration-d-objets-connectes/demo-nicegui-app-form-valid).

## Modèles de données

Les modèles sont accessibles avec `from models import Plante, Lumiere, TemperatureHumidite, Arrosage, Utilisateur`, comme dans les exemples du cours.

Les modèles dans `models/` décrivent les champs prévus pour l'échange avec l'API. Ce sont des classes Pydantic `BaseModel`, comme le modèle `Drone` de l'exemple du cours. Elles sont indépendantes de l'interface; leur présence ne branche pas encore les pages à l'API. Les pages affichent toujours les données fictives de `donnees_exemple.py`.

| Modèle | Rôle et utilisation prévue |
| --- | --- |
| `Plante` | État courant et paramètres d'une plante. Utilisé par la vue d'ensemble et la page des paramètres; `utilisateur_id` identifie son propriétaire. |
| `TemperatureHumidite` | Une mesure historique de température et d'humidité brute pour les graphiques. `plante_id` identifie la plante. |
| `Lumiere` | Une mesure historique de luminosité en lux pour les graphiques. `plante_id` identifie la plante. |
| `Arrosage` | Un événement d'arrosage, automatique si `auto` vaut `True`. L'API utilise l'historique pour calculer `arrosages_en_24h` dans `Plante`. |
| `Utilisateur` | Identité et champ `passwd` prévus pour l'authentification future; aucune authentification n'est encore implémentée. |

Les horodatages sont représentés par des chaînes en attendant le contrat précis de l'API. L'exemple fourni n'est pas un horodatage ISO 8601 valide; le format exact devra être confirmé lors de l'intégration. `humidite_brut` est une mesure brute : sa conversion en pourcentage et les unités de `intervalle_arrosage` et `seuil_humidite` restent à confirmer avec l'API. Aucun modèle ne calcule `arrosages_en_24h` dans le frontend.
