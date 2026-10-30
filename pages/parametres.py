from nicegui import ui

from layout import mise_en_page


def creer_page():
    @ui.page('/parametres')
    def page():
        with mise_en_page('Paramètres'):
            with ui.element('div').classes('two section'):
                with ui.card().classes('surface feature'):
                    ui.label('Paramètres du système').classes('card-heading')
                    ui.label('Valeurs utilisées par le système.').classes('body-copy')
                    ui.number('Seuil minimal d’humidité (%)', value=30, min=0, max=100).classes('setting-input').props('outlined disable')
                    ui.number('Seuil de luminosité (lux)', value=10000, min=1, max=200000).classes('setting-input').props('outlined disable')
                    ui.number('Durée d’arrosage (secondes · 3 max)', value=3, min=0.1, max=3, step=0.1).classes('setting-input').props('outlined disable')
                    ui.button('Enregistrer les paramètres').classes('primary-button').disable()
                with ui.element('div').classes('settings-stack'):
                    with ui.card().classes('surface feature'):
                        ui.label('Commandes').classes('card-heading')
                        for titre, texte in [('Arrosage automatique', 'Arrose 3 s quand l’humidité passe sous le seuil.'), ('Feu tricolore', 'Affiche l’état de la plante : vert, jaune ou rouge.')]:
                            with ui.row().classes('switch-row'):
                                with ui.column().classes('gap-1'):
                                    ui.label(titre).classes('small-heading')
                                    ui.label(texte).classes('description')
                                ui.switch(value=True).props('color=green').disable()
                    with ui.card().classes('surface feature'):
                        ui.label('Arrosage manuel').classes('card-heading')
                        ui.label('Durée : 3 secondes maximum. Refusé si le réservoir est insuffisant.').classes('body-copy')
                        ui.button('Arroser maintenant').classes('primary-button').disable()
                        ui.label('Commandes indisponibles dans cette maquette.').classes('subtle')
