from marshmallow import Schema, fields


class LoginValidator(Schema):
    # username = fields.Str(required=True)
    # surname = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)