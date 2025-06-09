from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 모델 등록 (꼭 해야 db.create_all()에서 인식됨)
from flask_start.models import post, user