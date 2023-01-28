from server.api import api
from flask_restx import Resource


np_grupo_alvo = api.namespace('grupo_alvo')



@np_grupo_alvo.route('/',methods=['GET','POST'])
@np_grupo_alvo.route('/<int:grupo_alvo_id>',methods=['GET','PUT','DELETE'])
class GrupoAlvo(Resource):
    def get(self,grupo_alvo_id=None):
        """Deve Retornar um grupo especifico ou todos os grupos"""
        if grupo_alvo_id:
            ...
        else:
            ...
        ...

    def post(self):
        """Deve criar um novo grupo"""
        ...
    
    def put(self):
        """Deve atualizar informacoes do grupo"""
        ...
    
    def delete(self):
        """Deve excluir o grupo"""
        ...

@np_grupo_alvo.route('/<int:grupo_alvo_id>/<int:user_id>',methods=['POST','DELETE'])
class GrupoAlvoUser(Resource):
    def post(self,grupo_alvo_id,user_id):
        """Deve Adicionar o Usuario no Grupo"""
        ...
    
    def delete(self,grupo_alvo_id,user_id):
        """Deve Remove o Usuario do Grupo"""
        ...