from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .models import * #AVISO: deixar abaixo da instacia do db - anti-loop

def init_db(app):
    db.init_app(app)
    db.create_all()
    Grupo.init_grupos()
