from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from scscraper import SCScraper
from werkzeug.exceptions import InternalServerError

# Create the global SQLAlchemy object.
db = SQLAlchemy()

# Create a global instance of the Social Catfish Scraper.
sc_scraper = SCScraper()


def create_app() -> Flask:
    """
    Create and configure an app.
    :returns: A Flask app.
    """
    config = Config()
    app = Flask('app')
    app.config['SECRET_KEY'] = config.get_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get_sql_alchemy_url()

    # Register error handlers.
    @app.errorhandler(InternalServerError)
    def handle_bad_request(e):
        return str(e), InternalServerError.code

    db.init_app(app)
    return app
