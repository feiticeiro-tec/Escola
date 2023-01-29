from ..database.models import Grupo, Usuario, GrupoAlvo, GrupoAlvoUser


def select_grupos(id=None):
    if id:
        return Grupo.query.get(id)
    return Grupo.query.all()


def select_users_group(grupo_id):
    return Usuario.query.filter(Usuario.grupo_id == grupo_id).all()


def select_grupo_alvo(id=None):
    if id:
        return GrupoAlvo.query.get(id)
    return GrupoAlvo.query.all()


def select_grupo_alvo_user(id=None):
    if id:
        return GrupoAlvoUser.query.get(id)
    return GrupoAlvoUser.query.all()
