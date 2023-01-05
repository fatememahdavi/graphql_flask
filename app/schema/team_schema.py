import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app import db
from app.model.team_model import TeamModel


class TeamObject(SQLAlchemyObjectType):
    class Meta:
        model = TeamModel
        interfaces = (graphene.relay.Node,)


class AddTeam(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    team = graphene.Field(lambda: TeamObject)

    def mutate(self, info, name):
        team = TeamModel(name=name)
        db.session.add(team)
        db.session.commit()
        return AddTeam(team=team)


class UpdateTeam(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    team = graphene.Field(lambda: TeamObject)

    def mutate(self, info, id, name):
        old_team = db.session.query(TeamModel).get(id)
        old_team.name = name
        db.session.commit()
        team = old_team
        return UpdateTeam(team=team)


class DeleteTeam(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    team = graphene.Field(lambda: TeamObject)

    def mutate(self, info, id):
        team = db.session.query(TeamModel).get(id)
        db.session.delete(team)
        db.session.commit()
        return DeleteTeam(team=team)
