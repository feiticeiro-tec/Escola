from ..database.models import Grupo

def select_grupos():
    return Grupo.query.all()
