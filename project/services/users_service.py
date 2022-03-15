from typing import Optional

from project.dao import UserDAO, User
from project.exceptions import ItemNotFound
from project.schemas import UserSchema
from project.services.base import BaseService
from project.tools.security import get_password_hash


class UsersService(BaseService):
    def get_one(self, uid: int):
        user = UserDAO(self._db_session).get_one(uid)
        return UserSchema().dump(user)

    def get_by_user_email(self, email) -> Optional[User]:
        user = UserDAO(self._db_session).get_by_user_email(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def create(self, **user):
        count = 1
        if len(UserDAO(self._db_session).get_all()) == 0:
            count = 2
        user = UserDAO(self._db_session).create({"username": user["username"], "surname": user["surname"], "email": user["email"], "password_hash": get_password_hash(user["password"]), "role_id": count})
        return user

    def write_refresh_token(self, user_email: str, refresh_token: str):
        user = UserDAO(self._db_session).write_refresh_token(user_email, refresh_token)
        return UserSchema().dump(user)
