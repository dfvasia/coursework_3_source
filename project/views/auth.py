from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import ValidationError
import project.tools as jwt
from . import genres_ns

from ..exceptions import ItemNotFound, DuplicateError
from ..schemas import LoginValidator
from ..services import UsersService
from project.setup_db import db
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthView(Resource):
    @genres_ns.response(201, "OK")
    @genres_ns.response(404, "User not found")
    @genres_ns.response(400, "Token not created")
    def post(self):
        """Create token"""
        try:
            validated_data = LoginValidator().load(request.json)
            user = UsersService(db.session).get_by_user_email(validated_data['email'])
            if not user:
                abort(404, message="User not found")
            token_data = jwt.JwtSchema().load({'user_id': user.id, 'role': user.role_id})
            a = jwt.JwtToken(token_data).get_tokens()
            b = UsersService(db.session).write_refresh_token(user.email, a["refresh_token"])
            print(b)
            return a
        except ValidationError as e:
            print(e)
            abort(400, message="Token not created")

    def put(self):
        """Update token"""
        try:
            r_token = request.json.get('refresh_token')
            data = jwt.JwtToken.decode_token(r_token)
            if not data:
                abort(404)
            token_data = jwt.JwtSchema().load({'user_id': data['user_id'], 'role': data['role']})
            return jwt.JwtToken(token_data).get_tokens(), 201
        except ValidationError as e:
            print(str(e))
            abort(400)


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    @genres_ns.response(201, "OK")
    @genres_ns.response(404, "User not found")
    @genres_ns.response(400, "Token not created")
    def post(self):
        try:
            user_id = UsersService(db.session).create(**LoginValidator().load(request.json))
            print(user_id)
            return {'id': user_id}, 201
        except ValidationError:
            raise BadRequest
        except DuplicateError:
            raise BadRequest('Username already exists')
