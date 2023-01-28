from .. import db
from datetime import datetime


class Default():
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text)
    utc_c = db.Column(db.DateTime)
    utc_u = db.Column(db.DateTime)
    db = db

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        

    def save(self):
        self.utc_u = datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def add(self):
        self.utc_c = datetime.utcnow()
        db.session.add(self)

    def frash(self):
        db.session.frash()
