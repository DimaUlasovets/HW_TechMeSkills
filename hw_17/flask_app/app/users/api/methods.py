import json

from app.models.base import User, db
from app.users.api.schema import UserSchema
from flask import Flask, request
from flask_restful import Resource


class UsersList(Resource):
    def get(self):
        users = User.query.all()
        user_schema = UserSchema()
        output = user_schema.dump(users, many=True)

        return output

    def post(self):
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            data = request.get_json()
        else:
            data = request.form

        user_schema = UserSchema()
        errors = user_schema.validate(data)

        if errors:
            return {"Missing or sending incorrect data", 500}
        else:
            user = User()
            for key in User.__table__.columns.keys():
                if key in data:
                    setattr(user, key, data[key])

        db.session.add(user)
        db.session.commit()

        return 201


class SingleUser(Resource):
    def get(self, pk):
        user = User.query.get(pk)
        user_schema = UserSchema()
        output = user_schema.dump(user, many=False)

        return output

    def delete(self, pk):
        user = User.query.get(pk)
        db.session.delete(user)
        db.session.commit()

        return {"note": "delete success"}

    def put(self, pk):

        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            data = request.get_json()
        else:
            return "Content-Type not supported!"

        user_schema = UserSchema()
        user = User.query.get(pk)
        errors = user_schema.validate(data)

        if errors:
            return {"Missing or sending incorrect data", 500}
        else:
            for key in User.__table__.columns.keys():
                if key in data:
                    setattr(user, key, data[key])

            db.session.commit()

        return 201
