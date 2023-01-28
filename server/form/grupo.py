from flask_restx import fields,reqparse
from .generic_model import GenericModel
from .usuario import FormUsuario
from ..api import api

class FormGrupo(GenericModel):
    model = api.model('Grupo',{
        'id':fields.Integer,
        'descricao':fields.String
    })
    model_list = api.model('Grupos',{
        'grupos':fields.List(fields.Nested(model))
    })

    @property
    def get(self):
        form = reqparse.RequestParser()
        form.add_argument('grupo_id',type=int)
        return form
    
    @property
    def get_response(self):
        return self.model_list
    

    @property
    def put(self):
        form = reqparse.RequestParser()
        form.add_argument('user',type=FormUsuario.user_validate,required=True)
        return form
    
    @property
    def put_response(self):
        return FormUsuario.model

class FormGrupoUsers(GenericModel):
    model_list = api.model('GruposUsers',{
        'usuarios':fields.List(fields.Nested(FormUsuario.model))
    })

    @property
    def get(self):
        form = reqparse.RequestParser()
        return form
    
    @property
    def get_response(self):
        return self.model_list