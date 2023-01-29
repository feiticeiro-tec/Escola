from functools import wraps
from flask import request
from server.api.utils import select_grupo_alvo_user
from flask_restx import abort


def valdiate_grupo_alvo_user_path(f):
    @wraps(f)
    def capture_args(*args, **kw):
        grupo_alvo = select_grupo_alvo_user(kw['grupo_alvo_user'])
        if not grupo_alvo:
            abort(404, 'Grupo alvo não encontrado!')
        return f(*args, **kw, grupo_alvo=grupo_alvo)
    return capture_args


def valdiate_grupo_alvo_user(f):
    @wraps(f)
    def capture_args(*args, **kw):
        grupo_alvo = select_grupo_alvo_user(
            request.values.get('grupo_alvo_user'))
        if not grupo_alvo:
            abort(404, 'Grupo alvo não encontrado!')
        return f(*args, **kw, grupo_alvo=grupo_alvo)
    return capture_args
