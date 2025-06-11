from flask import Flask, Blueprint, request, render_template, redirect, session
from flask_restx import Api, Resource, reqparse


bp = Blueprint('main', __name__, url_prefix='/')
app = Flask(__name__)
api = Api (app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
test_api = api.namespace('test', description='조회 api')


@bp.route('/')
def index():
    return 'Hello!'

@bp.route('/admin')
def admin_index():
    return "Hello! Your're admin."

@test_api.route('/')
class Test(Resource) :
    def get(self) :
        return 'Hello Flask!'

#이게 있어야 라우트와 swagger 동작함
app.register_blueprint(bp)

if __name__== '__main__':
    app.run()