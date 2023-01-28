from server.api import api
from flask_restx import Resource



np_sala = api.namespace('sala')



@np_sala.route('/',methods=['GET','POST'])
@np_sala.route('/<int:sala_id>',methods=['GET','PUT','DELETE'])
class Sala(Resource):
    def delete(self,sala_id):
        """Deve deletar a sala"""
        ...
    
    def get(self,sala_id=None):
        """Deve retornar um lista de salas filtradas ou não"""
        ...
    
    def post(self):
        """Deve criar uma nova sala"""
        ...
    
    def put(self,sala_id):
        """Deve atualizar as informações da sala"""
        ...
    
    

@np_sala.route('/<int:sala_id>/<int:user_id>',methods=['POST'])
@np_sala.route('/<int:sala_id>/<int:aluno_id>',methods=['GET','DELETE'])
class SalaAluno(Resource):
    
    def get(self,sala_id,aluno_id):
        """Deve retornar as informações do aluno na sala"""
        ...
    
    def post(self,sala_id,user_id):
        """Deve adicionar o usuario na sala"""
        ...
    
    def delete(self,sala_id,aluno_id):
        """Deve remove o aluno da sala a sala"""
        ...