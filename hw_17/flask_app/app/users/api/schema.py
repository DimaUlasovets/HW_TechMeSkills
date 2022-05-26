# from flask_marshmallow import Marshmallow
from app.models.base import User
from marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "user_name", "password")


class LoginUserSchema(Schema):
    class Meta:
        model = User
        fields = ("user_name", "password")
