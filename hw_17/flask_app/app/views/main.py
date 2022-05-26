import flask
from flask_login import current_user, login_required

main = flask.Blueprint("main", __name__, url_prefix="/")


@main.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")


@main.route("/profile", methods=["GET"])
@login_required
def profile():
    return flask.render_template("profile.html", name=current_user.user_name)
