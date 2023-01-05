import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from passlib.hash import pbkdf2_sha256 as sha256

from app import db
from app.model.user_model import UserModel


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class AddUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        teamId = graphene.Int(required=True)
        roleId = graphene.Int(required=True)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, name, password, email, phone, teamId, roleId):
        user = UserModel(
            name=name,
            password=sha256.hash(password),
            email=email,
            phone=phone,
            teamId=teamId,
            roleId=roleId,
        )
        db.session.add(user)
        db.session.commit()
        return AddUser(user=user)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        password = graphene.String(required=False)
        email = graphene.String(required=False)
        phone = graphene.String(required=False)
        teamId = graphene.Int(required=False)
        roleId = graphene.Int(required=False)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, id, name, password, email, phone, teamId, roleId):
        old_user = db.session.query(UserModel).get(id)
        if name:
            old_user.name = name
        if password:
            old_user.password = sha256.hash(password)
        if email:
            old_user.email = email
        if phone:
            old_user.phone = phone
        if teamId:
            old_user.teamId = teamId
        if roleId:
            old_user.roleId = roleId

        db.session.commit()
        user = old_user
        return UpdateUser(user=user)


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, id):
        user = db.session.query(UserModel).get(id)
        db.session.delete(user)
        db.session.commit()
        return DeleteUser(user=user)
