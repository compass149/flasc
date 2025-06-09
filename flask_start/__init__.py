from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Blueprint 등록
    from flask_start.routes import base_route
    app.register_blueprint(base_route.bp)

    return app