from nicegui import ui

from composants.carte_mesure import CarteMesure
from layout import mise_en_page
from models.donnees_exemple import MESURES


def creer_page():
    @ui.page('/')
    def page():
        with mise_en_page('Vue d’ensemble'):
            with ui.element('section').classes('section'):
                with ui.row().classes('section-title'):
                    ui.label('Les dernières mesures').classes('section-heading')
                    ui.label('Dernière mise à jour : 30 oct. 2026 · 16 h 10').classes('subtle')
                with ui.element('div').classes('metrics'):
                    for mesure in MESURES:
                        CarteMesure(mesure)
            with ui.element('div').classes('three section'):
                with ui.card().classes('surface feature'):
                    ui.label('ÉTAT DE LA PLANTE').classes('eyebrow')
                    ui.label('●  Normal · feu vert').classes('status-pill')
                    ui.label('Sol suffisamment humide, objectif de lumière atteint et réservoir suffisant.').classes('body-copy')
                    ui.html('<div class="legend"><span>🟢 Normal</span><span>🟡 À surveiller</span><span>🔴 Urgent</span></div>')
                with ui.card().classes('surface feature'):
                    ui.label('LUMIÈRE REÇUE AUJOURD’HUI').classes('eyebrow')
                    ui.label('6 h 10').classes('big')
                    ui.label('Objectif de lumière : 6 à 8 h par jour au-dessus de 10 000 lux.').classes('body-copy')
                    ui.html('<div class="progress light-progress" role="img" aria-label="6 h 10 sur 8 h"><i style="width:77%"></i></div>')
                    ui.label('Objectif minimal de 6 h atteint.').classes('subtle')
                with ui.card().classes('surface feature'):
                    ui.label('ARROSAGE').classes('eyebrow')
                    ui.label('Mode automatique activé').classes('card-heading')
                    for nom, valeur in [('Dernier arrosage', '30 oct. · 07 h 42'), ('Arrosages dans les dernières 24 h', '2'), ('Prochain arrosage automatique', 'Disponible')]:
                        with ui.row().classes('activity-row'):
                            ui.label(nom)
                            ui.label(valeur).classes('activity-value')
