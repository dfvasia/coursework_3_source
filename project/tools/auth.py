from functools import wraps
from typing import Dict, Any

from flask import request
from flask_restx import abort
from jwt import PyJWTError

from project.schemas import JwtSchema
from project.tools import JwtToken
from marshmallow import ValidationError


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            abort(401)
        try:
            data = JwtToken.decode_token(auth_header.split("Bearer ")[-1])
            data.pop('exp', None)
            token_data: Dict[str, Any] = JwtSchema().load(data)
            return func(*args, **kwargs, token_data=token_data)
        except (PyJWTError, ValidationError) as e:
            abort(401)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            abort(401)
        try:
            data = JwtToken.decode_token(auth_header.split("Bearer ")[-1])
            token_data: Dict[str, Any] = JwtSchema().load(data)
            if token_data['role'] != 'admin':
                abort(403)
            return func(*args, **kwargs, token_data=token_data)
        except (PyJWTError, ValidationError) as e:
            abort(401)
    return wrapper
