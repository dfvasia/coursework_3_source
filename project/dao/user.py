from typing import Optional

import sqlalchemy.exc

from project.dao.models import User

from ..exceptions import IncorrectData, DuplicateError


# CRUD
class UserDAO:
    def __init__(self, session):
        self._db_session = session
        self._roles = {'user', 'admin'}

    def get_by_user_email(self, email: str) -> Optional[User]:
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def update_role(self, email: str, role: str):
        if role not in self._roles:
            raise IncorrectData
        user = self.get_by_user_email(email)
        user.role = role
        return self._db_session(user)

    def write_refresh_token(self, email: str, refresh_token: str):
        user = self.get_by_user_email(email)
        user.refresh_token = refresh_token
        return self._db_session(user)

    def update_password(self, email: str, password_hash: str):
        user = self.get_by_user_email(email)
        user.password = password_hash
        return self._db_session(user)

    def get_one(self, uid) -> Optional[User]:
        return self._db_session.query(User).get(uid)

    def get_all(self):
        return self._db_session.query(User).all()

    def create(self, data):
        try:
            user = User(**data)
            self._db_session.add(user)
            self._db_session.commit()
            return user
        except sqlalchemy.exc.IntegrityError:
            raise DuplicateError

    def delete(self, uid):
        user = self.get_one(uid)
        self._db_session.delete(user)
        self._db_session.commit()

