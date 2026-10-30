from pydantic import BaseModel, Field


class Utilisateur(BaseModel):
    """Données d'utilisateur prévues pour la future authentification."""

    id: int
    nom: str
    passwd: str = Field(repr=False)
