"""Valeurs fictives pour la présentation, sans connexion au système."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Mesure:
    titre: str
    icone: str
    valeur: str
    unite: str
    description: str


MESURES = (
    Mesure('Humidité du sol', 'water_drop', '46', '%', 'Seuil d’arrosage : 30 %'),
    Mesure('Température du sol', 'device_thermostat', '22,4', '°C', 'Lecture toutes les 10 min'),
    Mesure('Luminosité', 'light_mode', '12 480', 'lux', 'Lumière suffisante dès 10 000 lux'),
    Mesure('Réservoir', 'water', 'Suffisant', '', 'La plante peut être arrosée'),
)
HEURES = ['16 h', '19 h', '22 h', '01 h', '04 h', '07 h', '10 h', '13 h', '16 h']
HUMIDITE = [44, 42, 40, 38, 36, 34, 50, 48, 46]
TEMPERATURE = [22.9, 21.4, 20.2, 19.5, 19, 18.6, 20.8, 23.6, 22.4]
LUMINOSITE = [400, 2100, 5600, 9600, 11900, 13800, 15200, 14600, 13900, 12900, 12480]
