import os

from app.models.base import db
from app.users.api.methods import LoginUser, SingleUser, UserRegister, UsersList
from app.users.api.sequre_check import login_manager
from app.views.auth import auth
from app.views.main import main
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)

    Migrate(app, db)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://d.ulasovets:lastochka1488@localhost:5432/flask_test"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SECRET_KEY"] = "3d6f45a5fc12445dbac2f59c3b6c7cb1"

    db.init_app(app)
    db.create_all(app=app)

    login_manager.init_app(app)

    api.add_resource(UsersList, "/api/users")
    api.add_resource(SingleUser, "/api/users/<int:pk>")
    api.add_resource(UserRegister, "/api/user-register")
    api.add_resource(LoginUser, "/api/user-login")

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
