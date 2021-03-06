from project.dao.models.base import BaseMixin
from project.setup_db import db


class Group(BaseMixin, db.Model):
    __tablename__ = 'group'
    name_role = db.Column(db.String, unique=True)

    def __repr__(self):
        return f"<Group '{self.name_role.title()}'>"


class User(BaseMixin, db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    role = db.relationship("Group")
    refresh_token = db.Column(db.String)

    def __repr__(self):
        return f"<User '{self.email.title()}'>"


class Fgu(db.Model):
    __tablename__ = 'fgu'

    __table_args__ = (db.PrimaryKeyConstraint('id_user', 'id_genre'),)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship('User')
    id_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    # genre = db.relationship('Genre')

    def __repr__(self):
        return f"<Fgu '{self.user.title() + self.genre.title()}'>"


class Fmu(db.Model):
    __tablename__ = 'fmu'

    __table_args__ = (db.PrimaryKeyConstraint('id_user', 'id_movie'),)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship('User')
    id_movie = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # movie = db.relationship('Movie')

    def __repr__(self):
        return f"<Fmu '{self.user.title() + self.movie.title()}'>"
