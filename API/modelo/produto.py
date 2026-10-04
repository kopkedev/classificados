from sqlalchemy import String, ForeignKey, Numeric, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .grupo import Base


class Produto(Base):
    __tablename__ = "produtos"

    id_produto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_grupo: Mapped[int] = mapped_column(ForeignKey("grupos.id"), nullable=False)
    descricao: Mapped[str | None] = mapped_column(String(255), nullable=True)
    usado: Mapped[bool] = mapped_column(default=False, nullable=False)
    preco: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    observacoes: Mapped[str | None] = mapped_column(Text, nullable=True)

    grupo = relationship("Grupo", back_populates="produtos")
