from .default import db, Default

class Grupo(db.Model, Default):
    __tablename__ = 'Grupo'

    def __init__(self,id, descricao):
        super().__init__(id=id,descricao=descricao)

    def init_grupos():
        try:
            db.session.add_all([
                Grupo(1,"ADM"),
                Grupo(2,"DIRETOR"),
                Grupo(3,"PROFESSOR"),
                Grupo(4,"ALUNO")
            ])
            db.session.commit()
        except:
            db.session.rollback()
        

