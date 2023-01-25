from .default import db, Default


class Sala(db.Model, Default):
    __tablename__ = 'Sala'

    professor_id = db.Column(
        db.Integer, db.ForeignKey('Usuario.id'), nullable=True)
    professo = db.relationship('Usuario', foreign_keys=[professor_id])

    alunos = db.relationship('Aluno', backref='Sala')

    def __init__(self, professor_id, nome=None):
        super().__init__(
            professor_id=professor_id,
            descricao=nome
        )
