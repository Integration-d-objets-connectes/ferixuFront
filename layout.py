from contextlib import contextmanager

from nicegui import ui

ROUTES = {'Vue d’ensemble': '/', 'Historique': '/historique', 'Paramètres': '/parametres'}


@contextmanager
def mise_en_page(page_active: str):
    ui.page_title(f'Pousse · {page_active}')
    ui.add_head_html('<link rel="stylesheet" href="/assets/style.css">')
    with ui.element('aside').classes('sidebar'):
        ui.link('✳ pousse.', '/').classes('brand')
        ui.label('VOTRE PLANTE').classes('nav-label')
        with ui.element('nav').classes('navigation'):
            for nom, route in ROUTES.items():
                lien = ui.link(nom, route).classes('nav-link')
                if nom == page_active:
                    lien.classes('active').props('aria-current=page')
        ui.label('Un peu d’attention,\nau bon moment.').classes('aside-bottom')
    with ui.element('main').classes('content'):
        with ui.element('header').classes('topbar'):
            ui.label(f'POUSSE / {page_active.upper()}')
            ui.label('MAQUETTE · DONNÉES D’EXEMPLE').classes('demo')
        ui.label(page_active).classes('page-title')
        yield
        with ui.element('footer').classes('footer'):
            ui.label('Pousse · Projet Ferixu')
            ui.label('Maquette non connectée au matériel · valeurs d’exemple')
