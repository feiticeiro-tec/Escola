from flask_restx import fields, reqparse
from .generic_model import GenericModel
from .usuario import FormUsuario
from .validators import Validators
from server.api import api
from server.api.utils import select_grupos

grupos = select_grupos()

class FormAuth(GenericModel):

    @property
    def post_response(self):
        return api.model('Auth', {'usuario': fields.Nested(FormUsuario.model)})

    @property
    def post(self):
        form = reqparse.RequestParser()
        form.add_argument('email', type=Validators.email(),
                          required=True, location='form')
        form.add_argument('senha', type=str, required=True, location='form')
        return form


class FormRegister(GenericModel):

    @property
    def post_response(self):
        return FormUsuario().model

    @property
    def post(self):
        form = reqparse.RequestParser()
        form.add_argument('email', type=FormUsuario.email_validate,
                          required=True, location='form')
        form.add_argument('senha', type=str, required=True, location='form')
        form.add_argument('confirmar_senha', type=Validators.match_value(
            'senha'), required=True, location='form')
        form.add_argument('grupo_id', choices=[str(grupo.id) for grupo in grupos], help=str([f'{grupo.id} - {grupo.descricao}' for grupo in grupos]))
        return form