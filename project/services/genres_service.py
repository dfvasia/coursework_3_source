from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def get_item_by_id(self, gid):
        genre = GenreDAO(self._db_session).get_by_id(gid)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)
