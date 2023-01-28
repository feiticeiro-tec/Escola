from flask_restx import Resource, marshal, abort
from server.api import api
from server.exceptions import NotFound, MatchError
from server.database.models import Usuario
from server.form import FormAuth,FormRegister

np_auth = api.namespace("auth")

form_auth = FormAuth()


@np_auth.route('/')
class Login(Resource):
    @form_auth.set_model_post(np_auth)
    def post(self):
        """Login de usuario."""
        data = form_auth.post.parse_args()
        try:
            user = Usuario.login(**data)
        except NotFound:
            abort(400, 'Email ou Senha Invalida!')
        except MatchError:
            abort(400, 'Email ou Senha Invalida!')

        return marshal(user, form_auth.post_response), 201


form_register = FormRegister()


@np_auth.route('/register')
class Register(Resource):
    @form_register.set_model_post(np_auth)
    def post(self):
        """Registro de usuario."""
        data = FormRegister().post.parse_args()
        user = Usuario(
            email=data['email'], senha=data['senha'], grupo_id=data['grupo_id'])
        user.add()
        user.save()
        return marshal(user, FormRegister().post_response), 201
