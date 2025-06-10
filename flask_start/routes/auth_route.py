from flask import Blueprint, request, redirect, render_template, flash, url_for
from flask_login import login_user, logout_user, login_required
from flask_start.models.user import User
from flask_start.models import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#회원가입
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = requset.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('auth.register'))
        
        # 사용자 생성 후 비밀번호 설정
        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully!')
        return redirect(url_for('auth.login'))
    return render_template('/user/register.html')

#로그인
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed.')
    return render_template('/user/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
