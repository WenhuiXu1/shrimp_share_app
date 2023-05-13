import os
from flask import Flask
from routes.memes_routes import memes_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
# import secrets

# api_key = secrets.token_hex(32)

# print(api_key)

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "default pretend key")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(memes_routes)
app.register_blueprint(users_routes)
app.register_blueprint(sessions_routes)