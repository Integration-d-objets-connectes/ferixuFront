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
