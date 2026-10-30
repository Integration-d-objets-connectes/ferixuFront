from nicegui import ui

from models.donnees_exemple import Mesure


class CarteMesure(ui.card):
    def __init__(self, mesure: Mesure) -> None:
        super().__init__()
        self.classes('surface metric')
        with self:
            ui.icon(mesure.icone).classes('metric-icon')
            ui.label(mesure.titre).classes('metric-title')
            with ui.row().classes('metric-value items-baseline gap-2'):
                ui.label(mesure.valeur).classes('word' if not mesure.unite else '')
                if mesure.unite:
                    ui.label(mesure.unite).classes('unit')
            if mesure.titre == 'Humidité du sol':
                ui.html('<div class="progress"><i style="width:46%"></i></div>')
            ui.label(mesure.description).classes('description')
