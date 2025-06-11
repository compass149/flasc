from flask_restx import Namespace, Resource

# Namespace 생성
test_ns = Namespace('test', description='테스트용 API')

# 라우트 설정
@test_ns.route('/')
class TestResource(Resource):
    def get(self):
        return {'message': 'Hello from RESTX!'}
 