from ..database.models import Grupo

def select_grupos(id=None):
    if id:
        return Grupo.query.get(id)
    return Grupo.query.all()
