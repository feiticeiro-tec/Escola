from flask_restx import Resource, marshal, abort
from server.api import api
from server.exceptions import NotFound, MatchError
from server.database.models import Usuario
from form import FormLogin, FormRegister

np_login = api.namespace("login")

form_login = FormLogin()


@np_login.route('/')
class Login(Resource):
    @form_login.set_model_post(np_login)
    def post(self):
        """Login de usuario."""
        data = FormLogin().post.parse_args()
        try:
            user = Usuario.login(**data)
        except NotFound:
            abort(400, 'Email ou Senha Invalida!')
        except MatchError:
            abort(400, 'Email ou Senha Invalida!')

        return marshal(user, FormLogin().post_response), 201


form_register = FormRegister()


@np_login.route('/register')
class Register(Resource):
    @form_register.set_model_post(np_login)
    def post(self):
        """Registro de usuario."""
        data = FormRegister().post.parse_args()
        user = Usuario(
            email=data['email'], senha=data['senha'], grupo_id=data['grupo_id'])
        user.add()
        user.save()
        return marshal(user, FormRegister().post_response), 201
