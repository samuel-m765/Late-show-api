from server.models.db import db
from server.models.appearance import Appearance  # if using in to_dict()

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
            "appearances": [appearance.to_dict() for appearance in self.appearances]
        }
