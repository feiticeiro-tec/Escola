import re
from flask_restx import fields, reqparse, inputs
from .generic_model import GenericModel
from .validators import Validators
from server.api import api
from server.database.models import Usuario


class FormUsuario(GenericModel):

    model = api.model('Usuario', {
        'id': fields.Integer,
        'email': fields.String,
        'grupo_id': fields.Integer,
        'primeiro_nome': fields.String,
        'ultimo_nome': fields.String,
        'nascimento': fields.Date,
        'estado': fields.String,
        'cidade': fields.String,
        'logradouro': fields.String,
        'numero': fields.String,
        'utc_c': fields.DateTime,
        'utc_u': fields.DateTime,
    })

    model_list = api.model('Usuarios', {
        'usuarios': fields.List(fields.Nested(model))
    })

    def email_validate(value) -> str:
        if not re.match(r'[\W|\D]+@[\W|\D]+.[\W|\D]+', value):
            raise ValueError('Email Invalido!')

        if Usuario.query.filter(Usuario.email == value).first():
            raise ValueError('Email já em uso!')

        return value

    def email_validate_optional(value) -> str:
        if not value:
            return value
        if not re.match(r'[\W|\D]+@[\W|\D]+.[\W|\D]+', value):
            raise ValueError('Email Invalido!')

        if Usuario.query.filter(Usuario.email == value).first():
            raise ValueError('Email já em uso!')

        return value

    def user_validate(id):
        try:
            id = int(id)
        except:
            raise ValueError('ID Invalido!')

        user = Usuario.query.get(id)
        if not user:
            raise ValueError('Usuario não existe!')
        return user

    @property
    def put_response(self):
        return self.model

    @property
    def put(self) -> reqparse.RequestParser:
        form = reqparse.RequestParser()
        form.add_argument('primeiro_nome', type=str, location='form')
        form.add_argument('ultimo_nome', type=str, location='form')
        form.add_argument('nascimento', type=inputs.datetime, location='form')
        form.add_argument('estado', type=str, location='form')
        form.add_argument('cidade', type=str, location='form')
        form.add_argument('logradouro', type=str, location='form')
        form.add_argument('numero', type=str, location='form')
        return form

    @property
    def patch_response(self):
        return self.model

    @property
    def patch(self) -> reqparse.RequestParser:
        form = reqparse.RequestParser()
        form.add_argument('senha_atual', type=str,
                          required=True, location='form')
        form.add_argument('nova_senha', type=str,
                          required=True, location='form')
        form.add_argument('confirmar_nova_senha', type=Validators.match_value(
            'nova_senha'), required=True, location='form')
        return form

    @property
    def get_response(self):
        return self.model_list

    @property
    def get(self) -> reqparse.RequestParser:
        form = reqparse.RequestParser()
        form.add_argument('user_id', type=int)
        return form

    @property
    def delete(self) -> reqparse.RequestParser:
        form = reqparse.RequestParser()
        return form
