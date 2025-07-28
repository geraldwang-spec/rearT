from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dotenv import load_dotenv
from app.models.StationClass import StationClass
# from app.api import bp as api_bp

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from app.api import routes
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)

    # with app.app_context():
    #     from . import auth, schema, routes
    #     app.register_blueprint(auth.bp)
    #     app.register_blueprint(routes.bp)
    #     # schema 會在後面用

    #     db.create_all()

    # @app.route('/')
    # def index():
    #     return 'Flask is running through Apach'

    # @app.route('/api')
    # def indexApi():
    #     return 'testapi'

    return app
