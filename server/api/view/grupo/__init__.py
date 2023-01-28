from flask_restx import Resource,Namespace,marshal,abort
from form import FormGrupo
from ...utils import select_grupos

np_grupo = Namespace('grupo')
form_grupos = FormGrupo()


@np_grupo.route('/')
@np_grupo.route('/<int:id>')
class Grupo(Resource):
    @form_grupos.set_model_get(np_grupo)
    def get(self,id=None):
        if id:
            grupo = select_grupos(id)
            if not grupo:
                abort(404,'Grupo não encontrado!')
            else:
                grupos = [grupo]
        else:
            grupos = select_grupos()
        
        return marshal(grupos,form_grupos.get_response)