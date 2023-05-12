from flask import Blueprint
from controllers.planets_controller import index, new, create, edit, update, delete

planets_routes = Blueprint('pmemes_routes', __name__)

planets_routes.route('/')(index)
planets_routes.route('/memes/new')(new)
planets_routes.route('/memes', methods = ['POST'])(create)
planets_routes.route('/memes/<id>/edit')(edit)
planets_routes.route('/memes/<id>', methods=["POST"])(update)
planets_routes.route('/memes/<id>/delete', methods=["POST"])(delete)