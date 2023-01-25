from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .models import *

def init_db(app):
    db.init_app(app)
    db.create_all()
