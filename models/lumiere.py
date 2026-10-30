from pydantic import BaseModel


class Lumiere(BaseModel):
    """Une mesure de lumière de l'historique d'une plante."""

    lux: float
    horodatage: str
    plante_id: int
