from typing import Dict, Any

from flask import request, Response
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

# users_ns = Namespace('users')
from project.exceptions import DuplicateError
from project.schemas import UserSchema, LoginValidator
from project.services import UsersService
from project.setup_db import db
from project.tools import login_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @login_required
    def get(self, token_data: Dict[str, Any]):
        return UserSchema().dump(UsersService(db.session).get_one(token_data['user_id']))

    def post(self):
        try:
            user_id = UsersService.create(**LoginValidator().load(request.json))
            return {'id': user_id}, 201
        except ValidationError:
            raise BadRequest
        except DuplicateError:
            raise BadRequest('Username already exists')


# @users_ns.route('/<int:gid>')
# class UsersView(Resource):
#     def get(self, gid: int):
#         user = user_service.get_one(gid)
#
#         return UserSchema().dump(user), 200
#
#     def put(self, gid):
#         reg_json = request.json
#         reg_json["id"] = gid
#
#         user_service.get_update(reg_json)
#
#         return "", 204
#
#     def patch(self, gid):
#         reg_json = request.json
#         reg_json["id"] = gid
#
#         user_service.update_partial(reg_json)
#
#         return "", 204
#
#     def delete(self, gid: int):
#         user_service.delete(gid)
#
#         return "", 204
