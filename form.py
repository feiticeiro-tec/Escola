from flask import request
from flask_restx import Resource,marshal,abort,reqparse,inputs
from server.database.models import Usuario
from server.api import api
from flask_restx import fields
import re
from functools import wraps


class Validators():
    def match_value(field):
        def match(value):
            if not value == request.values[field]:
                raise ValueError(f'{field} não deu match!')
            return value
        return match
    def email():
        return inputs.regex('[\W|\D]+@[\W|\D]+')

class GenericModel:
    def set_model_get(self,namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.get_response,code=200)
            @namespace.expect(self.get)
            def capture_args(*args,**kw):
                return f(*args,**kw)

            return capture_args
        return capture_func

    def set_model_delete(self,namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.delete_response,code=200)
            @namespace.expect(self.delete)
            def capture_args(*args,**kw):
                return f(*args,**kw)

            return capture_args
        return capture_func

    def set_model_put(self,namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.put_response,code=200)
            @namespace.expect(self.put)
            def capture_args(*args,**kw):
                return f(*args,**kw)

            return capture_args
        return capture_func

    def set_model_post(self,namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.post_response,code=201)
            @namespace.expect(self.post)
            def capture_args(*args,**kw):
                return f(*args,**kw)

            return capture_args
        return capture_func

class FormUsuario:

    @property
    def model(self):
        return api.model('Usuario',{'email':fields.String})
    
    def email_validate(value):
        value = value.strip()
        if not re.match('[\W|\D]+@[\W|\D]+',value):
            raise ValueError('Email Invalido!')
        
        if Usuario.query.filter(Usuario.email==value).first():
            raise ValueError('Email já em uso!')
        
        return value

class FormLogin:

    @property
    def post_response(self):
        return api.model('Auth',{'email':fields.String})
    
    @property
    def post(self):
        form = reqparse.RequestParser()
        form.add_argument('email',type=Validators.email(),required=True,location='form')
        form.add_argument('senha',type=str,required=True,location='form')
        return form

class FormRegister(GenericModel):

    @property
    def post_response(self):
        return FormUsuario().model

    @property
    def post(self):
        form = reqparse.RequestParser()
        form.add_argument('email',type=FormUsuario.email_validate,required=True,location='form')
        form.add_argument('senha',type=str,required=True,location='form')
        form.add_argument('confirmar_senha',type=Validators.match_value('senha'),required=True,location='form')
        return form