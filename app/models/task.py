from sqlalchemy import ForeignKey
from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def todict(self):
        task_dict = {"id": self.task_id,
                    "title": self.title,
                    "description": self.description,
                    "is_complete": bool(self.completed_at)}
        if self.goal_id:
            task_dict["goal_id"] = self.goal_id
        return task_dict

    @classmethod
    def fromdict(cls, data_dict):
        task = Task(title = data_dict["title"],
                    description = data_dict["description"],
                    completed_at = data_dict.get("completed_at"),
                    goal_id = data_dict.get("goal_id"))
        return task