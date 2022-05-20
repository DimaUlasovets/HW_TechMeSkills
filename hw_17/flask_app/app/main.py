import os

from app.users.api.methods import SingleUser, UsersList
from app.views.views import home_blueprint
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    db = SQLAlchemy(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://d.ulasovets:lastochka1488@localhost:5432/flask_test"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)
    db.create_all(app=app)

    api.add_resource(UsersList, "/api/users")
    api.add_resource(SingleUser, "/api/users/<int:pk>")

    app.register_blueprint(home_blueprint)

    return app
