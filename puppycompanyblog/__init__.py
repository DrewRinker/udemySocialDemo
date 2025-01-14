# pupyycompanyblog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages

app = Flask(__name__)

# Database setup
db = SQLAlchemy(app)
Migrate(db, app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Blueprints
app.register_blueprint(core)
app.register_blueprint(error_pages)

# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
