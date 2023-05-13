from flask import Blueprint
from controllers.sessions_controller import new, create, delete

sessions_routes = Blueprint('sessions_routes', __name__)

sessions_routes.route('/sessions/new')(new)
sessions_routes.route('/sessions', methods=["POST"])(create)
sessions_routes.route('/sessions/delete', methods = ["POST"])(delete)