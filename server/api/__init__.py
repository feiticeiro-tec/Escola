from flask_restx import Api

api = Api()

def init_api(app):
    api.init_app(app)
    from server.api.view import auth,usuario,grupo,grupo_alvo,noticia,sala,teste
    return api