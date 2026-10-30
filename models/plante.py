from pydantic import BaseModel


class Plante(BaseModel):
    """État et paramètres d'une plante associés à un utilisateur."""

    id: int
    nom: str
    temperature_c: float
    humidite_brut: float
    eau_vide: bool
    lux: float
    dernier_arrosage: str
    arrosages_en_24h: int
    horodatage: str
    intervalle_arrosage: float
    seuil_humidite: float
    seuil_luminosite: float
    utilisateur_id: int
