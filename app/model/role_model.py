from app import db


class RoleModel(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(360), unique=True, nullable=False)

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def _clone(self):
        return RoleModel(id=self.id, name=self.name,)
