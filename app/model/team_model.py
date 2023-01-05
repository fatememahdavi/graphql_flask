from app import db


class TeamModel(db.Model):
    __tablename__ = "team"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(360), unique=True, nullable=False)

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def _clone(self):
        return TeamModel(id=self.id, name=self.name,)
