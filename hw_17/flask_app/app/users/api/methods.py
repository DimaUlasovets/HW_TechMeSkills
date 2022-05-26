import json

from app.models.base import User, db
from app.users.api.schema import LoginUserSchema, UserSchema
from flask import Flask, flash, redirect, request, url_for
from flask_login import login_user
from flask_restful import Resource
from werkzeug.security import check_password_hash, generate_password_hash


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
            for key in data:
                values = data[key]

                if key == "password":
                    values = generate_password_hash(data[key], method="sha256")

                setattr(user, key, values)

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


class UserRegister(Resource):
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
            user_email = User.query.filter_by(email=data["email"]).first()
            user_name = User.query.filter_by(user_name=data["user_name"]).first()
            if user_email:
                flash("Email address already exists")
                return redirect(url_for("auth.signup"))
            elif user_name:
                flash("Username already exists")
                return redirect(url_for("auth.signup"))
            else:
                user = User()

                for key in data:
                    values = data[key]

                    if key == "password":
                        values = generate_password_hash(data[key], method="sha256")

                    setattr(user, key, values)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"), 201)


class LoginUser(Resource):
    def post(self):
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            data = request.get_json()
        else:
            data = request.form

        login_user_schema = LoginUserSchema()
        errors = login_user_schema.validate(data)
        remember = True if request.form.get("remember") else False

        if errors:
            return {"Missing or sending incorrect data", 500}
        else:
            user = User.query.filter_by(user_name=data["user_name"]).first()
            if not user or not check_password_hash(user.password, data["password"]):
                flash("Please check your login details and try again.")
                return redirect(url_for("auth.login"))

        login_user(user, remember=remember)

        return redirect(url_for("main.profile"))
