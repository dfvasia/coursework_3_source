from project.dao.models import Director


# CRUD
class DirectorDAO:
    def __init__(self, session):
        self._db_session = session

    def get_by_id(self, did: int):
        return self._db_session.query(Director).filter(Director.id == did).one_or_none()

    def get_one(self, did: int):
        return self._db_session.query(Director).get(did)

    def get_all(self):
        return self._db_session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        return self._db_session(director)

    def delete(self, did: int):
        director = self.get_one(did)
        self._db_session(director)
