from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    surname = fields.Str()
    email = fields.Email(required=True)
    password_hash = fields.Str(load_only=True)
    role = fields.Str()
    role_id = fields.Int()
    refresh_token = fields.Str()


class GroupSchema(Schema):
    id = fields.Int(required=True)
    name_role = fields.Str(required=True)


class FguSchema(Schema):

    id_user = fields.Int(required=True)
    id_genre = fields.Int(required=True)


class FmuSchema(Schema):

    id_user = fields.Int(required=True)
    id_movie = fields.Int(required=True)
