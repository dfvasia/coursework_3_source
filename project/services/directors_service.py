from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def get_item_by_id(self, did):
        director = DirectorDAO(self._db_session).get_by_id(did)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_movies(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)

    def get_update(self, data):
        did = data.get("id")
        director = DirectorDAO(self._db_session).get_one(did)

        director.name = data.get("name")

        return DirectorSchema().dump(director)

    def create(self, data):
        director = DirectorDAO(self._db_session).create(data)
        return DirectorSchema().dump(director)

    def delete(self, did):
        director = DirectorDAO(self._db_session).delete(did)
        return DirectorSchema().dump(director)
