from flask_restx import Resource,marshal,abort
from server.api import api
from form import FormGrupo,FormGrupoUsers
from ...utils import select_grupos,select_users_group
from functools import wraps

np_grupo = api.namespace('grupo')
form_grupos = FormGrupo()
form_grupos_users = FormGrupoUsers()


@np_grupo.route('/',methods=['GET'])
@np_grupo.route('/<int:grupo_id>',methods=['PUT'])
class Grupo(Resource):
    def validate_id_group(f):
        @wraps(f)
        def capture_args(*args,**kw):
            grupo = select_grupos(kw['grupo_id'])
            if not grupo:
                abort(404,'Grupo não encontrado!')
            return f(*args,**kw,grupo=grupo)
        return capture_args
    
    @form_grupos.set_model_get(np_grupo)
    def get(self):
        """Vai retornar uma lista de grupos"""
        grupo_id = form_grupos.get.parse_args()['grupo_id']
        if grupo_id:
            grupo = select_grupos(grupo_id)
            if not grupo:
                abort(404,'Grupo não encontrado!')
            else:
                grupos = {'grupos':[grupo]}
        else:
            grupos = {'grupos':select_grupos()}
        
        return marshal(grupos,form_grupos.get_response)
    
    @form_grupos.set_model_put(np_grupo)
    @validate_id_group
    def put(self,grupo_id,grupo):
        """Vai atualizar o grupo do usuario."""
        data= form_grupos.put.parse_args()
        user = data['user']
        user.grupo_id = grupo_id
        user.save()
        return marshal(user,form_grupos.put_response)

@np_grupo.route('/<int:grupo_id>/usuarios/')
class GrupoUsers(Resource):
    @form_grupos_users.set_model_get(np_grupo)
    def get(self,grupo_id):
        """Vai retonar uma lista de usuarios que pertence ao grupo"""
        users= select_users_group(grupo_id)
        return marshal({"usuarios":users},form_grupos_users.get_response)