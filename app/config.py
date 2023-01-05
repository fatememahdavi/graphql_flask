"""Flask configuration variables."""
import logging

from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    print(FLASK_APP)
    FLASK_DEBUG = environ.get("FLASK_DEBUG")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = environ.get("SQLALCHEMY_COMMIT_ON_TEARDOWN")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

    logging.basicConfig(
        filename=environ.get("LOG_FILE"),
        level=logging._nameToLevel.get(environ.get("LOG_LEVEL")),
    )
