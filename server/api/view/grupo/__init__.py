from flask_restx import Resource,marshal,abort
from server.api import api
from form import FormGrupo,FormGrupoUsers
from ...utils import select_grupos,select_users_group

np_grupo = api.namespace('grupo')
form_grupos = FormGrupo()
form_grupos_users = FormGrupoUsers()


@np_grupo.route('/')
@np_grupo.route('/<int:grupo_id>')
class Grupo(Resource):
    @form_grupos.set_model_get(np_grupo)
    def get(self,grupo_id=None):
        if grupo_id:
            grupo = select_grupos(id)
            if not grupo:
                abort(404,'Grupo não encontrado!')
            else:
                grupos = {'grupos':[grupo]}
        else:
            grupos = {'grupos':select_grupos()}
        
        return marshal(grupos,form_grupos.get_response)

@np_grupo.route('/usuarios/<int:grupo_id>')
class GrupoUsers(Resource):
    @form_grupos_users.set_model_get(np_grupo)
    def get(self,grupo_id):
        users= select_users_group(grupo_id)
        return marshal({"usuarios":users},form_grupos_users.get_response)