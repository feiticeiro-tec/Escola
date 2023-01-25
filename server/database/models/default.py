from .. import db
from datetime import datetime
import pdb

class Default():
    id = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.Text)
    utc_c = db.Column(db.DateTime)
    utc_u = db.Column(db.DateTime)

    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        self.utc_c = datetime.utcnow()
    
    def save(self):
        self.utc_u = datetime.utcnow()
        db.session.commit()
    
    def add(self):
        db.session.add(self)
    
    def frash(self):
        db.session.frash()
