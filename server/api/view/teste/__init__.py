from server.api import api
from flask_restx import Resource


np_teste = api.namespace('teste')


@np_teste.route('/',methods=['GET','POST'])
@np_teste.route('/<int:teste_id>',methods=['GET','PUT','DELETE'])
class Teste(Resource):
    
    def post(self):
        """Deve criar um novo teste"""
        ...
    def get(self,teste_id=None):
        """Deve retorna uma lista de testes filtrados ou n."""
        ...
    def put(self,teste_id):
        """Deve Atualizar as informações do teste"""
        ...
    def delete(self,teste_id):
        """Deve excluir as informações do teste"""
        ...

@np_teste.route('/<int:teste_id>',methods=['GET','POST'])
@np_teste.route('/<int:teste_id>/<int:pergunta_id>',methods=['GET','PUT','DELETE'])
class TestePergunta(Resource):
    def post(self,teste_id):
        """Deve criar uma nova pergunta"""
        ...
    def get(self,teste_id,pergunta_id=None):
        """Deve retorna uma lista de perguntas filtradas ou n"""
        ...
    def put(self,teste_id,pergunta_id):
        """Deve Atualizar a pergunta"""
        ...
    def delete(self,teste_id,pergunta_id):
        """Deletar uma pergunta"""
        ...

@np_teste.route('/<int:teste_id>/<int:pergunta_id>',methods=['GET','POST'])
@np_teste.route('/<int:teste_id>/<int:pergunta_id>/<int:resposta_id>',methods=['GET','PUT','DELETE'])
class TesteResposta(Resource):
    def post(self,teste_id,pergunta_id):
        """Deve criar uma nova resposta"""
        ...
    def get(self,teste_id,pergunta_id,resposta_id=None):
        """Deve retorna uma lista de respostas filtradas ou n"""
        ...
    def put(self,teste_id,pergunta_id,resposta_id):
        """Deve Atualizar a pergunta"""
        ...
    def delete(self,teste_id,pergunta_id,resposta_id):
        """Deletar uma pergunta"""
        ...
