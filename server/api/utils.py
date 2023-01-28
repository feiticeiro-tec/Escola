from ..database.models import Grupo,Usuario

def select_grupos(id=None):
    if id:
        return Grupo.query.get(id)
    return Grupo.query.all()

def select_users_group(grupo_id):
    return Usuario.query.filter(Usuario.grupo_id==grupo_id).all()