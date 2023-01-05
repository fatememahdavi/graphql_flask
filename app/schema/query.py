import graphene

from app.model.role_model import RoleModel
from app.model.team_model import TeamModel
from app.model.user_model import UserModel
from app.schema.role_schema import RoleObject
from app.schema.team_schema import TeamObject
from app.schema.user_schema import UserObject


class Query(graphene.ObjectType):
    users = graphene.List(UserObject)
    getUserById = graphene.Field(UserObject, id=graphene.Int())
    teams = graphene.List(TeamObject)
    getTeamByName = graphene.Field(TeamObject, name=graphene.String())
    roles = graphene.List(RoleObject)
    getRoleByName = graphene.Field(RoleObject, name=graphene.String())

    def resolve_getUserById(self, info, id):
        query = UserObject.get_query(info)
        return query.filter(UserModel.id == id).first()

    def resolve_getTeamByName(self, info, name):
        query = TeamObject.get_query(info)
        return query.filter(TeamModel.name == name).first()

    def resolve_getRoleByName(self, info, name):
        query = RoleObject.get_query(info)
        return query.filter(RoleModel.name == name).first()

    def resolve_users(self, info):
        query = UserObject.get_query(info)
        return query.all()

    def resolve_teams(self, info):
        query = TeamObject.get_query(info)
        return query.all()

    def resolve_roles(self, info):
        query = RoleObject.get_query(info)
        return query.all()
