from .default import db, Default


class GrupoAlvo(db.Model, Default):
    __tablename__ = 'GrupoAlvo'

    def __init__(self, descricao):
        super().__init__(descricao=descricao)

    def update(self, data):
        for key, valor in data.items():
            if valor:
                setattr(self, key, valor)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
