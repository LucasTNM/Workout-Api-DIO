from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento') # type: ignore