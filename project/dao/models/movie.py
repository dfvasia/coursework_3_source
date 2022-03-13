from project.dao.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = 'movie'

    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    # genre = db.relationship("Genre", primaryjoin="genre_id == Genre.id")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    # director = db.relationship("Director", primaryjoin="director_id == Director.id")

    def __repr__(self):
        return F"<Movie '{self.title.title()}'>"

