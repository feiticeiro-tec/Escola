from server.api import api
from flask_restx import Resource

np_noticia = api.namespace('noticia')


@np_noticia.route('/',methods=['GET','POST'])
@np_noticia.route('/<int:noticia_id>',methods=['GET','PUT','DELETE'])
class Noticia(Resource):
    def get(self,noticia_id=None):
        """Deve Retornar uma lista de noticias filtrada ou não"""
        ...
    
    def post(self):
        """Deve Criar um noticia com um grupo alvo"""
        ...
    
    def put(self):
        """Deve atualizar as informações da noticia e grupo alvo"""
        ...
    
    def delete(self):
        """Deve excluir a noticia"""