# from flask import Flask
# from flask_migrate import Migrate
# from flask_start.models import db, user
# from flask_login import LoginManager, current_user

# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
    
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qna.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SECRET_KEY'] = 'supersecretkey'


#     # DB 초기화
#     db.init_app(app)
    
#     # Blueprint 등록
#     from flask_start.routes import base_route, auth_route
#     app.register_blueprint(base_route.bp)
#     app.register_blueprint(auth_route.bp)


#     return app

from flask import Flask
from flask_migrate import Migrate
from flask_start.models import db
from flask_login import LoginManager, current_user
from flask_start.models.user import User

migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qna.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from flask_start.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    # context processor 등록
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    return app
