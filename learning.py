__author__ = "Fred B"

from flask import Blueprint
learning_blueprint = Blueprint("learning", __name__)


@learning_blueprint.route("/<string:name>")
def index(name):
    return f"hello, {name}!"
