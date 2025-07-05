from uuid import UUID
from sqlalchemy import DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta') # type: ignore
    categoria_id: Mapped[UUID] = mapped_column(ForeignKey('categorias.id'), nullable=False)
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta') # type: ignore
    centro_treinamento_id: Mapped[UUID] = mapped_column(ForeignKey('centros_treinamento.id'), nullable=False)
