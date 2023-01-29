from flask import request
from flask_restx import abort
from server.database.models import Usuario as User
from functools import wraps


def validate_user_path(f):
    @wraps(f)
    def capture_args(*args, **kw):
        user: User = User.query.get(kw['user_id'])
        if not user:
            abort(404, 'Usuario não encontrado!')
        return f(*args, **kw, user=user)
    return capture_args


def validate_user(f):
    @wraps(f)
    def capture_args(*args, **kw):
        user: User = User.query.get(request.values.get('user_id'))
        if not user:
            abort(404, 'Usuario não encontrado!')
        return f(*args, **kw, user=user)
    return capture_args
