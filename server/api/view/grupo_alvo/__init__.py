from server.api import api
from flask_restx import Resource
from server.api.form.grupo_alvo import FormGrupoAlvo
from server.api.utils import select_grupo_alvo
from flask import request
from functools import wraps

np_grupo_alvo = api.namespace('grupo_alvo')

form_grupo_alvo = FormGrupoAlvo()


@np_grupo_alvo.route('/', methods=['GET', 'POST'])
@np_grupo_alvo.route('/<int:grupo_alvo_id>', methods=['PUT', 'DELETE'])
class GrupoAlvo(Resource):

    def valdiate_grupo_alvo(f):
        @wraps(f)
        def capture_args(*args, **kw):
            grupo_alvo = select_grupo_alvo(request.values.get('grupo_alvo_id'))
            return f(*args, **kw, grupo_alvo=grupo_alvo)
        return capture_args

    @form_grupo_alvo.set_model_get(np_grupo_alvo)
    def get(self):
        """Deve Retornar um grupo especifico ou todos os grupos"""
        grupo_alvo_id = form_grupo_alvo.get.parse_args()['grupo_alvo_id']
        if grupo_alvo_id:
            ...
        else:
            ...
        ...

    @form_grupo_alvo.set_model_post(np_grupo_alvo)
    def post(self):
        """Deve criar um novo grupo"""
        ...

    @form_grupo_alvo.set_model_put(np_grupo_alvo)
    @valdiate_grupo_alvo
    def put(self, grupo_alvo_id, grupo_alvo):
        """Deve atualizar informacoes do grupo"""
        ...

    @valdiate_grupo_alvo
    def delete(self, grupo_alvo_id, grupo_alvo):
        """Deve excluir o grupo"""
        ...


@np_grupo_alvo.route('/<int:grupo_alvo_id>/<int:user_id>', methods=['POST', 'DELETE'])
class GrupoAlvoUser(Resource):
    def post(self, grupo_alvo_id, user_id):
        """Deve Adicionar o Usuario no Grupo"""
        ...

    def delete(self, grupo_alvo_id, user_id):
        """Deve Remove o Usuario do Grupo"""
        ...
