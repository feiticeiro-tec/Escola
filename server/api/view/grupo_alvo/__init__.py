from server.api import api
from flask_restx import Resource, marshal, abort
from server.api.form.grupo_alvo import FormGrupoAlvo
from server.api.utils import select_grupo_alvo
from flask import request
from functools import wraps
from server.api.decoradores import validate_user, valdiate_grupo_alvo_path, valdiate_grupo_alvo_user_path
from server.database.models import GrupoAlvo as GA, GrupoAlvoUser as GAU

np_grupo_alvo = api.namespace('grupo_alvo')

form_grupo_alvo = FormGrupoAlvo()


@np_grupo_alvo.route('/', methods=['GET', 'POST'])
@np_grupo_alvo.route('/<int:grupo_alvo_id>', methods=['PUT', 'DELETE'])
class GrupoAlvo(Resource):

    @form_grupo_alvo.set_model_get(np_grupo_alvo)
    def get(self):
        """Deve Retornar um grupo especifico ou todos os grupos"""
        grupo_alvo_id = form_grupo_alvo.get.parse_args()['grupo_alvo_id']
        grupos = {
            "grupo_alvo": [select_grupo_alvo(grupo_alvo_id)] if grupo_alvo_id else select_grupo_alvo()
        }
        return marshal(grupos)

    @form_grupo_alvo.set_model_post(np_grupo_alvo)
    def post(self):
        """Deve criar um novo grupo"""
        data = form_grupo_alvo.post.parse_args()
        grupo = GA(**data)
        grupo.add()
        grupo.save()
        return marshal(grupo, form_grupo_alvo.model)

    @form_grupo_alvo.set_model_put(np_grupo_alvo)
    @valdiate_grupo_alvo_path
    def put(self, grupo_alvo_id, grupo_alvo: GA):
        """Deve atualizar informacoes do grupo"""
        data = form_grupo_alvo.put.parse_args()
        grupo_alvo.update(data)
        grupo_alvo.save()
        return marshal(grupo_alvo, form_grupo_alvo.model)

    @valdiate_grupo_alvo_path
    def delete(self, grupo_alvo_id, grupo_alvo: GA):
        """Deve excluir o grupo"""
        grupo_alvo.delete()
        return {}, 204


@np_grupo_alvo.route('/<int:grupo_alvo_id>', methods=['POST'])
@np_grupo_alvo.route('/<int:grupo_alvo_user_id>', methods=['DELETE'])
class GrupoAlvoUser(Resource):
    @valdiate_grupo_alvo_path
    @validate_user
    def post(self, grupo_alvo_id, grupo_alvo, user):
        """Deve Adicionar o Usuario no Grupo"""
        grupo = GAU(grupo_alvo_id=grupo_alvo_id, user_id=user.id)
        grupo.add()
        grupo.save()

    @valdiate_grupo_alvo_user_path
    def delete(self, grupo_alvo_user_id, grupo_alvo_user):
        """Deve Remove o Usuario do Grupo"""
        grupo_alvo_user.delete()
        return {}, 204
