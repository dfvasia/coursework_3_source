from marshmallow import Schema, fields


class LoginValidator(Schema):
    username = fields.Str(required=False)
    surname = fields.Str(required=False)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
