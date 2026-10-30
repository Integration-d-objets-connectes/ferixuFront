from pydantic import BaseModel


class TemperatureHumidite(BaseModel):
    """Une mesure de température et d'humidité brute de l'historique."""

    temperature_c: float
    humidite_brut: float
    horodatage: str
    plante_id: int
