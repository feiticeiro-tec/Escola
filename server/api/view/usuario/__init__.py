from flask import jsonify
from flask_restx import Resource, marshal, abort
from server.api import api
from form import FormUsuario
from server.database.models import Usuario as User
from functools import wraps


np_usuario = api.namespace('usuario')
form_usuario = FormUsuario()



@np_usuario.route('/',methods=['GET'])
@np_usuario.route('/<int:user_id>',methods=['PUT','PATCH','DELETE'])
class Usuario(Resource):
    @form_usuario.set_model_get(np_usuario)
    def get(self):
        """Vai retornar uma lista de usuarios."""
        user_id = form_usuario.get.parse_args()['user_id']
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            if not user:
                abort(404, 'Usuario não encontrado!')
            usuarios = [user]
        else:
            usuarios = User.query.all()
        return marshal({'usuarios': usuarios}, form_usuario.get_response)

    def validate_user(f):
        @wraps(f)
        def capture_args(*args,**kw):
            user:User = User.query.get(kw['user_id'])
            if not user:
                abort(404, 'Usuario não encontrado!')
            return f(*args,**kw, user=user)
        return capture_args

    @form_usuario.set_model_put(np_usuario)
    @validate_user
    def put(self,user_id,user):
        """vai atualizar as informações do usuario."""
        data = form_usuario.put.parse_args()
        user.update(data)
        user.save()
        
        return marshal(user, form_usuario.put_response)
    
    @form_usuario.set_model_patch(np_usuario)
    @validate_user
    def patch(self,user_id,user):
        """Vai atualizar a senha do usuario"""
        data = form_usuario.patch.parse_args()
        if not user.check_password(data['senha_atual']):
            abort(400,{"errors":{'senha_atual':"Senha Invalida!"}})
        user.set_password(data['nova_senha'])
        user.save()
        return marshal(user, form_usuario.patch_response)
    
    @validate_user
    def delete(self,user_id,user):
        """Vai deletar o usuario"""
        user.delete()
        return {},204