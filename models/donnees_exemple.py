"""Valeurs fictives pour la présentation, sans connexion au système."""
from pydantic import BaseModel


class Mesure(BaseModel):
    titre: str
    icone: str
    valeur: str
    unite: str
    description: str


MESURES = (
    Mesure(titre='Humidité du sol', icone='water_drop', valeur='46', unite='%', description='Seuil d’arrosage : 30 %'),
    Mesure(titre='Température du sol', icone='device_thermostat', valeur='22,4', unite='°C', description='Lecture toutes les 10 min'),
    Mesure(titre='Luminosité', icone='light_mode', valeur='12 480', unite='lux', description='Lumière suffisante dès 10 000 lux'),
    Mesure(titre='Réservoir', icone='water', valeur='Suffisant', unite='', description='La plante peut être arrosée'),
)
HEURES = ['16 h', '19 h', '22 h', '01 h', '04 h', '07 h', '10 h', '13 h', '16 h']
HUMIDITE = [44, 42, 40, 38, 36, 34, 50, 48, 46]
TEMPERATURE = [22.9, 21.4, 20.2, 19.5, 19, 18.6, 20.8, 23.6, 22.4]
LUMINOSITE = [400, 2100, 5600, 9600, 11900, 13800, 15200, 14600, 13900, 12900, 12480]
