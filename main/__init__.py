from flask import Flask
from .config.config import Config
from .extension.extension import db, migrate, bcrypt, jwt, marshmallow
from main.v1.auth.routes import auth_blueprint
from main.v1.items.routes import items_blueprint
from .database.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    marshmallow.init_app(app)

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(items_blueprint, url_prefix='/items')

  
    
    return app
