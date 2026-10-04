from sqlalchemy.orm import Session
from sqlalchemy import select
from modelo.grupo import Grupo

#comentario de teste para github test
class RepGrupo:
    def __init__(self, db: Session):
        self.db = db


    def listar(self):
        return self.db.scalars(select(Grupo)).all()


    def buscar_por_id(self, grupo_id: int):
        return self.db.get(Grupo, grupo_id)

    def cadastrar(self, descricao: str | None = None):
        grupo = Grupo(descricao=descricao)
        self.db.add(grupo)
        self.db.commit()
        self.db.refresh(grupo)
        return grupo

    def alterar(self, grupo_id: int, descricao: str | None = None):
        grupo = self.buscar_por_id(grupo_id)
        if not grupo:
            return None
        if descricao is not None:
            grupo.descricao = descricao
        self.db.commit()
        return grupo

    def excluir(self, grupo_id: int):
        grupo = self.buscar_por_id(grupo_id)
        if not grupo:
            return False
        self.db.delete(grupo)
        self.db.commit()
        return True
