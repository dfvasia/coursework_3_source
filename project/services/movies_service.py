from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas import MovieSchema
from project.services.base import BaseService


class MoviesService(BaseService):
    def get_item_by_id(self, gid):
        movie = MovieDAO(self._db_session).get_by_id(gid)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all_movies(self):
        movies = MovieDAO(self._db_session).get_all()
        return MovieSchema(many=True).dump(movies)
