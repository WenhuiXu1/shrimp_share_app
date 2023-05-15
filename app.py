import os
from flask import Flask
from routes.memes_routes import memes_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from dotenv import load_dotenv
# from flask_wtf.file import FileField

# profile_pic = FileField("Profile Pic")

load_dotenv()

# db_url = os.environ.get('DATABASE_URL')

app = Flask(__name__)
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

app.secret_key = os.environ.get('FLASK_SECRET_KEY')

app.register_blueprint(memes_routes)
app.register_blueprint(users_routes)
app.register_blueprint(sessions_routes)