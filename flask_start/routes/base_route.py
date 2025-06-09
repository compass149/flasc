from flask import Blueprint, request, render_template, redirect, session

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'Hello!'

@bp.route('/admin')
def admin_index():
    return "Hello! Your're admin."