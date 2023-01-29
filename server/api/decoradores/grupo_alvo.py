from functools import wraps
from flask import request
from server.api.utils import select_grupo_alvo
from flask_restx import abort


def valdiate_grupo_alvo_path(f):
    @wraps(f)
    def capture_args(*args, **kw):
        grupo_alvo = select_grupo_alvo(kw['grupo_alvo_id'])
        if not grupo_alvo:
            abort(404, 'Grupo alvo não encontrado!')
        return f(*args, **kw, grupo_alvo=grupo_alvo)
    return capture_args


def valdiate_grupo_alvo(f):
    @wraps(f)
    def capture_args(*args, **kw):
        grupo_alvo = select_grupo_alvo(request.values.get('grupo_alvo_id'))
        if not grupo_alvo:
            abort(404, 'Grupo alvo não encontrado!')
        return f(*args, **kw, grupo_alvo=grupo_alvo)
    return capture_args
