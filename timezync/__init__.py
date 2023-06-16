from flask import Flask
from config import Config
from timezync.database import db

from timezync.rest.api import rest_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

   # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(rest_bp)

    return app