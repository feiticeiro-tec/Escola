from .default import db, Default


class GrupoAlvo(db.Model, Default):
    __tablename__ = 'GrupoAlvo'

    def __init__(self, id, descricao):
        super().__init__(id=id, descricao=descricao)
