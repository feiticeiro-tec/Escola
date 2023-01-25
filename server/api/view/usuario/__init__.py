from flask_restx import Resource, marshal, abort
from server.api import api
from form import FormUsuario
from server.database.models import Usuario as User


np_usuario = api.namespace('Usuario')
form_usuario = FormUsuario()


@np_usuario.route('/')
@np_usuario.route('/<int:id>')
class Usuario(Resource):
    @form_usuario.set_model_get(np_usuario)
    def get(self, id=None):
        if id:
            usuario = User.query.filter(User.id == id).first()
            if not usuario:
                abort(400, 'Usuario não encontrado!')
            usuarios = [usuario]
        else:
            usuarios = User.query.all()
        return marshal({'usuarios': usuarios}, form_usuario.model_list)
