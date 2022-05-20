import flask

home_blueprint = flask.Blueprint("", __name__, url_prefix="/")


@home_blueprint.route("/", methods=["GET"])
def get_home_page():
    return flask.render_template("index.html")


@home_blueprint.route("/register", methods=["GET"])
def get_register_page():
    return flask.render_template("registration.html")
