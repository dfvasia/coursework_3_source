from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import Genre


class GenreDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, gid: int):
        return self._db_session.query(Genre).filter(Genre.id == gid).one_or_none()

    def get_all(self):
        return self._db_session.query(Genre).all()

    def get_one(self, gid: int):
        return self._db_session.query(Genre).get(gid)

    def create(self, data):
        genre = Genre(**data)
        return self._db_session(genre)

    def delete(self, gid: int):
        genre = self.get_one(gid)
        self._db_session(genre)
