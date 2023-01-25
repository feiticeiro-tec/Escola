from .default import db, Default
from server.exceptions import NotFound, MatchError


class Usuario(db.Model, Default):
    __tablename__ = 'Usuario'
    email = db.Column(db.String(255), unique=True)
    senha = db.Column(db.String(255))
    professor = db.Column(db.Boolean, default=False)

    def __init__(self, email, senha, professor):
        super().__init__(
            email=email,
            senha=senha,
            professor=int(professor)
        )

    @staticmethod
    def login(email, senha):
        user = Usuario.query.filter(Usuario.email == email).first()
        if not user:
            raise NotFound('Usuario não encontrado!')

        if not user.check_password(senha):
            raise MatchError('Senha invalida!')

        return user

    def check_password(self, senha):
        return self.senha == senha
