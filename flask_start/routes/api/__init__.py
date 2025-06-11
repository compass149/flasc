from flask_restx import Api
from flask_start.routes.api.test_api import test_ns

api = Api(
    title='QnA API',
    version='1.0',
    description='Flask-RESTX 기반 Swagger 문서',
    doc='/api-docs'  # Swagger UI 주소
)

# 각 네임스페이스 등록
api.add_namespace(test_ns, path='/api/test')