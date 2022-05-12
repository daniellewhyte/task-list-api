from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def todict(self):
        return {"id": self.goal_id,
                "title": self.title}