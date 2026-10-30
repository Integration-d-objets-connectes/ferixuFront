from dataclasses import dataclass, field


@dataclass
class Utilisateur:
    """Données d'utilisateur prévues pour la future authentification."""

    id: int
    nom: str
    passwd: str = field(repr=False)
