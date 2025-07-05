from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria') # type: ignore