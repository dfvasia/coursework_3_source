from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    # genre = fields.Nested(GenreSchema, many=True)
    director_id = fields.Int()
    # director = fields.Nested(DirectorSchema, many=True)

