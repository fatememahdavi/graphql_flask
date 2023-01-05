from app import db
from app.model.role_model import RoleModel
from app.model.team_model import TeamModel


class UserModel(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(360), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(360), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    teamId = db.Column(
        db.Integer,
        db.ForeignKey(TeamModel.id, ondelete="CASCADE", onupdate="CASCADE"),
        unique=False,
        nullable=False,
    )
    roleId = db.Column(
        db.Integer,
        db.ForeignKey(RoleModel.id, ondelete="CASCADE", onupdate="CASCADE"),
        unique=False,
        nullable=False,
    )

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
            "phone": self.phone,
            "teamId": self.teamId,
            "roleId": self.roleId,
        }

    def _clone(self):
        return UserModel(
            id=self.id,
            name=self.name,
            password=self.password,
            email=self.email,
            phone=self.phone,
            teamId=self.teamId,
            roleId=self.roleId,
        )
