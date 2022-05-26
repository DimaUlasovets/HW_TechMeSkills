import flask
from flask_login import login_required, login_user, logout_user

auth = flask.Blueprint("auth", __name__, url_prefix="/")


@auth.route("login", methods=["GET"])
def login():
    return flask.render_template("login.html")


@auth.route("signup", methods=["GET"])
def signup():
    return flask.render_template("signup.html")


@auth.route("logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return flask.render_template("index.html")
