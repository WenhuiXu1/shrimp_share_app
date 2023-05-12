from flask import Blueprint
from controllers.memes_controller import index, new, create, edit, update, delete

memes_routes = Blueprint('memes_routes', __name__)

memes_routes.route('/')(index)
memes_routes.route('/memes/new')(new)
memes_routes.route('/memes', methods = ['POST'])(create)
memes_routes.route('/memes/<id>/edit')(edit)
memes_routes.route('/memes/<id>', methods=["POST"])(update)
memes_routes.route('/memes/<id>/delete', methods=["POST"])(delete)