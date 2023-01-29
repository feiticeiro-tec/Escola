from .default import db, Default


class GrupoAlvoUser(db.Model, Default):
    __tablename__ = 'GrupoAlvoUser'
    user_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    grupo_alvo_id = db.Column(db.Integer, db.ForeignKey('GrupoAlvo.id'))

    def __init__(self, user_id, grupo_alvo_id):
        super().__init__(user_id=user_id, grupo_alvo_id=grupo_alvo_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
