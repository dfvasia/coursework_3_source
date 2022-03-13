from typing import Optional

from project.dao import UserDAO, User
from project.exceptions import ItemNotFound
from project.schemas import UserSchema
from project.services.base import BaseService


class UsersService(BaseService):
    def get_one(self, uid):
        user = UserDAO(self._db_session).get_one(uid)
        return UserSchema().dump(user)

    def get_by_user_email(self, email: str) -> Optional[User]:
        user = UserDAO(self._db_session).get_by_user_email(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def create(self, **user):
        user = UserDAO(self._db_session).create({"username": user["username"], "surname": user["surname"], "email": user["email"], "password_hash": get_password_hash(user["password"]), "role_id": 1})
        return UserSchema().dump(user)

    def write_refresh_token(self, email: str, refresh_token: str) -> Optional[User]:
        user = UserDAO(self._db_session).write_refresh_token(email, refresh_token)
        return UserSchema().dump(user)
