from nicegui import ui

from layout import mise_en_page
from models.donnees_exemple import HEURES, HUMIDITE, LUMINOSITE, TEMPERATURE


def creer_page():
    @ui.page('/historique')
    def page():
        with mise_en_page('Historique'):
            with ui.element('section').classes('section'):
                ui.label('Historique des mesures').classes('section-heading section-title')
                with ui.element('div').classes('history-grid'):
                    with ui.card().classes('surface history-card'):
                        ui.label('Humidité et température du sol').classes('small-heading')
                        ui.label('Dernières 24 heures · humidité (%) à gauche, température (°C) à droite.').classes('description')
                        ui.echart({'color': ['#426f4b', '#b5683f'], 'tooltip': {'trigger': 'axis'}, 'legend': {'bottom': 0}, 'grid': {'left': 48, 'right': 48, 'top': 30, 'bottom': 60}, 'xAxis': {'type': 'category', 'data': HEURES}, 'yAxis': [{'type': 'value', 'min': 0, 'max': 100, 'name': '%'}, {'type': 'value', 'min': 10, 'max': 30, 'name': '°C'}], 'series': [{'name': 'Humidité', 'type': 'line', 'data': HUMIDITE}, {'name': 'Température', 'type': 'line', 'yAxisIndex': 1, 'data': TEMPERATURE, 'lineStyle': {'type': 'dashed'}}]}).classes('chart')
                    with ui.card().classes('surface history-card'):
                        ui.label('Luminosité').classes('small-heading')
                        ui.label('Aujourd’hui, moyenne par heure (lux). Ligne pointillée : seuil de 10 000 lux.').classes('description')
                        ui.echart({'tooltip': {'trigger': 'axis'}, 'grid': {'left': 60, 'right': 20, 'top': 30, 'bottom': 50}, 'xAxis': {'type': 'category', 'data': [f'{h:02d} h' for h in range(6, 17)]}, 'yAxis': {'type': 'value', 'max': 16000}, 'series': [{'name': 'Luminosité (lux)', 'type': 'bar', 'data': [{'value': valeur, 'itemStyle': {'color': '#64825c' if valeur >= 10000 else '#a17d29'}} for valeur in LUMINOSITE], 'markLine': {'symbol': 'none', 'data': [{'yAxis': 10000, 'name': 'Seuil 10 000 lux'}], 'lineStyle': {'color': '#95752f', 'type': 'dashed'}}}]}).classes('chart')
