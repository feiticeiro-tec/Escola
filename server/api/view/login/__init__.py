from flask import jsonify
from flask_restx import Resource, marshal, abort, reqparse, inputs
from flask_restx._http import HTTPStatus
from server.api import api
from server.exceptions import NotFound, MatchError
import pdb
from server.database.models import Usuario
import re
from form import FormLogin, FormRegister

np_login = api.namespace("login")

form_login = FormLogin()


@np_login.route('/')
class Login(Resource):
    @form_login.set_model_post(np_login)
    def post(self):
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
        data = FormRegister().post.parse_args()
        user = Usuario(
            email=data['email'], senha=data['senha'], professor=data['professor'])
        user.add()
        user.save()
        return marshal(user, FormRegister().post_response), 201
