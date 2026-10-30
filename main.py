from pathlib import Path

from nicegui import app, ui

from pages import historique, parametres, vue_ensemble

app.add_static_files('/assets', Path(__file__).parent / 'assets')
vue_ensemble.creer_page()
historique.creer_page()
parametres.creer_page()

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(title='Pousse · Ferixu', reload=False)
