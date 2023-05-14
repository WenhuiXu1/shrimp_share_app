from flask import Blueprint
from controllers.memes_controller import index, new, create, edit, update, delete, like, comment_new, create_comment, delete_comment, upload

memes_routes = Blueprint('memes_routes', __name__)

memes_routes.route('/')(index)
memes_routes.route('/memes/new')(new)
memes_routes.route('/memes', methods = ['POST'])(create)
memes_routes.route('/memes/<id>/edit')(edit)
memes_routes.route('/memes/<id>', methods=["POST"])(update)
memes_routes.route('/memes/<id>/delete', methods=["POST"])(delete)
memes_routes.route('/memes/<id>/likes', methods=["POST"])(like)
memes_routes.route('/comments/<id>/new')(comment_new)
memes_routes.route('/comments/<id>/add', methods=["POST"])(create_comment)
memes_routes.route('/comments/<id>/delete', methods=["POST"])(delete_comment)
memes_routes.route('/upload', methods=["POST"])(upload)