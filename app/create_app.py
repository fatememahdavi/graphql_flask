"""Initialize Flask app."""
import logging

from flask import Flask
from flask_migrate import Migrate

from app import db
from app.config import Config

_log = logging.getLogger(__name__)


def create_app():
    """Construct the core application."""
    _log.info("start create the app.")

    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder="./build",
        static_url_path="/",
    )
    migrate = Migrate(app, db)

    app.config.from_object(Config)

    db.init_app(app)

    return app
