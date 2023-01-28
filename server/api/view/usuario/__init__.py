from flask import jsonify
from flask_restx import Resource, marshal, abort
from server.api import api
from form import FormUsuario
from server.database.models import Usuario as User
from functools import wraps


np_usuario = api.namespace('Usuario')
form_usuario = FormUsuario()



@np_usuario.route('/')
class Usuario(Resource):
    @form_usuario.set_model_get(np_usuario)
    def get(self, id=None):
        if id:
            user = User.query.filter(User.id == id).first()
            if not user:
                abort(404, 'Usuario não encontrado!')
            usuarios = [user]
        else:
            usuarios = User.query.all()
        return marshal({'usuarios': usuarios}, form_usuario.get_response)

@np_usuario.route('/<int:id>')
class UsuarioControl(Usuario):
    def validate_user(f):
        @wraps(f)
        def capture_args(*args,**kw):
            user:User = User.query.get(kw['id'])
            if not user:
                abort(404, 'Usuario não encontrado!')
            return f(*args,**kw, user=user)
        return capture_args

    @form_usuario.set_model_put(np_usuario)
    @validate_user
    def put(self,id,user):
        data = form_usuario.put.parse_args()
        user.update(data)
        user.save()

        return marshal(user, form_usuario.put_response)
    
    @form_usuario.set_model_patch(np_usuario)
    @validate_user
    def patch(self,id,user):
        data = form_usuario.patch.parse_args()
        if not user.check_password(data['senha_atual']):
            abort(400,{"errors":{'senha_atual':"Senha Invalida!"}})
        user.set_password(data['nova_senha'])
        user.save()
        return marshal(user, form_usuario.patch_response)
    
    @validate_user
    def delete(self,id,user):
        user.delete()
        return {},204