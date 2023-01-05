import graphene

from app.schema.role_schema import AddRole, UpdateRole, DeleteRole
from app.schema.team_schema import AddTeam, UpdateTeam, DeleteTeam
from app.schema.user_schema import AddUser, UpdateUser, DeleteUser


class Mutation(graphene.ObjectType):
    addUser = AddUser.Field()
    addTeam = AddTeam.Field()
    addRole = AddRole.Field()
    deleteUser = DeleteUser.Field()
    deleteTeam = DeleteTeam.Field()
    deleteRole = DeleteRole.Field()
    updateUser = UpdateUser.Field()
    updateTeam = UpdateTeam .Field()
    updateRole = UpdateRole.Field()
