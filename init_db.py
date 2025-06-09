from flask_start import create_app
from flask_start.models import db

from flask_start.models.post import Post, Comment, File

app = create_app()

#wsl에 python init_db.py 적어서 실행하기
with app.app_context():
    db.create_all()
    print("Tables created:", db.metadata.tables.keys())