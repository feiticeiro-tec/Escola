from flask_restx import Api

api = Api()

from .view import *

def init_api(app):
    api.init_app(app)
    return api