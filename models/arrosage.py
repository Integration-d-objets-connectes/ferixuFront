from dataclasses import dataclass


@dataclass
class Arrosage:
    """Un événement d'arrosage, automatique ou manuel."""

    auto: bool
    horodatage: str
    plante_id: int
