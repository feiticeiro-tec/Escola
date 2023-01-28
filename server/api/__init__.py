from flask_restx import Api

api = Api()

def init_api(app):
    api.init_app(app)
    from server.api.view import login,usuario,grupo
    return api