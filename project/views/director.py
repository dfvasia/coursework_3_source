from flask import request
from flask_restx import Resource, Namespace, abort

from project.exceptions import ItemNotFound
from project.services import DirectorsService
from project.setup_db import db
from project.tools import login_required, admin_required


directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        return DirectorsService(db.session).get_all_movies()

    @directors_ns.response(201, "OK")
    @admin_required
    def post(self):
        reg_json = request.json
        s = DirectorsService(db.session).create(reg_json)
        s_t = f"/director/{s}"
        return "", 201, {'location': s_t}


@directors_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, director_id: int):
        try:
            return DirectorsService(db.session).get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")

    @directors_ns.response(204, "OK")
    @directors_ns.response(404, "Director not found")
    @admin_required
    def put(self, director_id):
        try:
            return DirectorsService(db.session).get_update(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")

    @directors_ns.response(204, "OK")
    @directors_ns.response(404, "Director not found")
    @admin_required
    def delete(self, director_id: int):
        try:
            return DirectorsService(db.session).delete(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
