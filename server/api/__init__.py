from flask_restx import Api

api = Api()

from .view import * #AVISO: deixar abaixo da instacia da api - anti-loop

def init_api(app):
    api.init_app(app)
    return api