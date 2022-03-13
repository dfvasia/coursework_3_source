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
