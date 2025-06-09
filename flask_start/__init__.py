from flask import Flask
from flask_migrate import Migrate
from flask_start.models import db, user
from flask_login import LoginManager

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qna.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'


    # DB 초기화
    db.init_app(app)
    
    # Blueprint 등록
    from flask_start.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)


    return app