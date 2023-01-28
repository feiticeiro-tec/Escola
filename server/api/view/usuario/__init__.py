from flask import jsonify
from flask_restx import Resource, marshal, abort
from server.api import api
from form import FormUsuario
from server.database.models import Usuario as User


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

    @staticmethod
    def validate_user(id,form_method) -> tuple[User,dict]:
        data = form_method.parse_args()
        user:User = User.query.get(id)
        if not user:
            abort(404, 'Usuario não encontrado!')
        return user,data

    @form_usuario.set_model_put(np_usuario)
    def put(self,id):
        user, data = self.validate_user(id=id,form_method=form_usuario.put)
        user.update(data)
        user.save()

        return marshal(user, form_usuario.put_response)
    
    @form_usuario.set_model_patch(np_usuario)
    def patch(self,id):
        user, data = self.validate_user(id=id,form_method=form_usuario.patch)
        if not user.check_password(data['senha_atual']):
            return jsonify({
                "errors":{
                    'senha_atual':"Senha Invalida!"
                }
            }),400
        user.set_password(data['nova_senha'])
        user.save()
        return marshal(user, form_usuario.patch_response)


