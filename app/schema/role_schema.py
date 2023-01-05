import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app import db
from app.model.role_model import RoleModel


class RoleObject(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (graphene.relay.Node,)


class AddRole(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    role = graphene.Field(lambda: RoleObject)

    def mutate(self, info, name):
        role = RoleModel(name=name)
        db.session.add(role)
        db.session.commit()
        return AddRole(role=role)


class UpdateRole(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    role = graphene.Field(lambda: RoleObject)

    def mutate(self, info, id, name):
        old_role = db.session.query(RoleModel).get(id)
        old_role.name = name
        db.session.commit()
        role = old_role
        return UpdateRole(role=role)


class DeleteRole(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    role = graphene.Field(lambda: RoleObject)

    def mutate(self, info, id):
        role = db.session.query(RoleModel).get(id)
        db.session.delete(role)
        db.session.commit()
        return DeleteRole(role=role)



