from sqlalchemy import desc

from project.dao.models import Movie


# CRUD
class MovieDAO:
    def __init__(self, session):
        self._db_session = session

    def found_film(self, movie):
        if 'director_id' in movie and 'genre_id' in movie:
            director_id = movie['director_id']
            genre_id = movie['genre_id']
            return self._db_session.query(Movie).filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()
        if 'director_id' in movie:
            director_id = movie['director_id']
            return self._db_session.query(Movie).filter(Movie.director_id == director_id).all()
        if 'genre_id' in movie:
            genre_id = movie['genre_id']
            return self._db_session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_id(self, gid: int):
        return self._db_session.query(Movie).filter(Movie.id == gid).one_or_none()

    def get_one(self, mid):
        return self._db_session.query(Movie).get(mid)

    def get_all(self):
        return self._db_session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        return self._db_session(movie)

    def delete(self, mid):
        movie = self.get_one(mid)
        self._db_session(movie)

    def get_filter(self, limit: int, offset: int, status: str):
        if limit > 0 and status == 'new':
            return self._db_session.query(Movie).order_by(desc(Movie.year)).limit(limit).offset(offset).all()
        elif limit > 0:
            return self._db_session.query(Movie).limit(limit).offset(offset).all()
        elif status == 'new':
            return self._db_session.query(Movie).order_by(desc(Movie.year)).all()
