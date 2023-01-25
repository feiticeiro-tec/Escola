from .default import db, Default


class Grupo(db.Model, Default):
    __tablename__ = 'Grupo'

    def __init__(self, descricao):
        super().__init__(descricao=descricao)
