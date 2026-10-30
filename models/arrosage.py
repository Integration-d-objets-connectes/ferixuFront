from pydantic import BaseModel


class Arrosage(BaseModel):
    """Un événement d'arrosage, automatique ou manuel."""

    auto: bool
    horodatage: str
    plante_id: int
