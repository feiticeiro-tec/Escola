from .generic_model import GenericModel
from flask_restx import reqparse, fields
from server.api import api


class FormGrupoAlvo(GenericModel):
    model = api.model('GrupoAlvo', {
        'id': fields.Integer,
        'descricao': fields.String
    })
    model_list = api.model('GropoAlvoList', {
        "grupo_alvo": fields.List(fields.Nested(model))
    })

    @property
    def get(self):
        form = reqparse.RequestParser()
        form.add_argument('grupo_alvo_id', type=int)
        return form

    @property
    def get_response(self):
        return self.model

    @property
    def post(self):
        form = reqparse.RequestParser()
        form.add_argument('descricao', required=True,
                          type=str, location='form')
        return form

    @property
    def post_response(self):
        return self.model

    @property
    def put(self):
        form = reqparse.RequestParser()
        form.add_argument('grupo_alvo_id', type=int, location='form')
        form.add_argument('descricao', type=str, location='form')
        return form

    @property
    def put_response(self):
        return self.model
