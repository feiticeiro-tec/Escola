from .default import db, Default


class Aluno(db.Model, Default):
    __tablename__ = 'Aluno'
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'Usuario.id'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('Sala.id'), nullable=False)

    def __init__(self, usuario_id, sala_id):
        super().__init__(
            usuario_id=usuario_id,
            sala_id=sala_id
        )
