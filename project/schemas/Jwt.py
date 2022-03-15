from marshmallow import Schema, fields


class JwtSchema(Schema):
    user_id = fields.Int(required=True)
    role = fields.Int(required=True)
