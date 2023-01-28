from .default import db, Default
from server.exceptions import NotFound, MatchError


class Usuario(db.Model, Default):
    __tablename__ = 'Usuario'
    email = db.Column(db.String(255), unique=True)
    senha = db.Column(db.String(255))
    grupo_id = db.Column(db.Integer,db.ForeignKey('Grupo.id'))

    primeiro_nome = db.Column(db.String(255))
    ultimo_nome = db.Column(db.String(255))
    nascimento = db.Column(db.Date)
    estado = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(255))


    def __init__(self, email, senha, grupo_id):
        super().__init__(
            email=email,
            grupo_id=int(grupo_id)
        )
        self.set_password(senha)
    

    @staticmethod
    def login(email, senha):
        user = Usuario.query.filter(Usuario.email == email).first()
        if not user:
            raise NotFound('Usuario não encontrado!')

        if not user.check_password(senha):
            raise MatchError('Senha invalida!')

        return user

    def set_password(self,senha):
        self.senha = senha

    def check_password(self, senha):
        return self.senha == senha
    
    def update(self,data):
        for key,valor in data.items():
            if key == 'senha':
                continue
            if valor:
                setattr(self,key,valor)
        
        senha = data.get('senha')
        if senha:
            self.senha = senha