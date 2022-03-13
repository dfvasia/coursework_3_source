from flask import request
from flask_restx import Resource, Namespace, reqparse
# from flask_restful import reqparse
from project.services import MoviesService
from project.setup_db import db
from project.tools import login_required, admin_required

movies_ns = Namespace('movies')
parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('status', type=str)


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(parser)
    @login_required
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all Movies"""
        req_args = parser.parse_args()
        if any(req_args.values()):
            return MoviesService(db.session).get_filter_movies(req_args)
        else:
            return MoviesService(db.session).get_all_movies()

    @admin_required
    def post(self):
        reg_json = request.json

        s = MoviesService(db.session).create(reg_json)
        s_t = f"/director/{s}"
        return "", 201, {'location': s_t}


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    @login_required
    def get(self, mid: int):
        movie = MoviesService(db.session).get_one(mid)

        return MovieSchema().dump(movie), 200

    @admin_required
    def put(self, mid):
        reg_json = request.json
        reg_json["id"] = mid

        MoviesService(db.session).get_update(reg_json)

        return "", 204

    @admin_required
    def patch(self, mid):
        reg_json = request.json
        reg_json["id"] = mid

        MoviesService(db.session).get_update_partial(reg_json)

        return "", 204

    @admin_required
    def delete(self, mid: int):
        MoviesService(db.session).delete(mid)

        return "", 204
