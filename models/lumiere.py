from dataclasses import dataclass


@dataclass
class Lumiere:
    """Une mesure de lumière de l'historique d'une plante."""

    lux: float
    horodatage: str
    plante_id: int
