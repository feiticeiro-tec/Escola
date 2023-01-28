from flask import request
from flask_restx import Resource, marshal, abort, reqparse, inputs
from server.database.models import Usuario
from server.api import api
from flask_restx import fields
import re
from functools import wraps


class Validators():
    def match_value(field) -> callable:
        def match(value) -> str:
            if not value == request.values[field]:
                raise ValueError(f'{field} não deu match!')
            return value
        return match
    
    def match_value_optional(field) -> callable:
        def match(value) -> str:
            if not request.values[field]:
                return ''
            if not value == request.values[field]:
                raise ValueError(f'{field} não deu match!')
            return value
        return match

    def email() -> inputs.regex:
        return inputs.regex(r'[\W|\D]+@[\W|\D]+.[\W|\D]+')


class GenericModel:
    def set_model_get(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.get_response, code=200)
            @namespace.expect(self.get)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_delete(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.delete_response, code=200)
            @namespace.expect(self.delete)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_put(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.put_response, code=200)
            @namespace.expect(self.put)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_post(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.post_response, code=201)
            @namespace.expect(self.post)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func
    
    def set_model_patch(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.patch_response, code=201)
            @namespace.expect(self.patch)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func


class FormUsuario(GenericModel):

    model = api.model('Usuario', {
        'id':fields.Integer,
        'email': fields.String,
        'professor': fields.Boolean,
        'primeiro_nome': fields.String,
        'ultimo_nome': fields.String,
        'nascimento': fields.Date,
        'estado': fields.String,
        'cidade': fields.String,
        'logradouro': fields.String,
        'numero': fields.String,
        'utc_c':fields.DateTime,
        'utc_u':fields.DateTime,
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
        form.add_argument('senha_atual', type=str, required=True, location='form')
        form.add_argument('nova_senha', type=str, required=True, location='form')
        form.add_argument('confirmar_nova_senha', type=Validators.match_value('nova_senha'),required=True, location='form')
        return form

    @property
    def get_response(self):
        return self.model_list

    @property
    def get(self) -> reqparse.RequestParser:
        form = reqparse.RequestParser()
        return form


class FormLogin(GenericModel):

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
        form.add_argument('professor', choices=('0', '1'))
        return form
