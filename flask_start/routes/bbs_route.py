from flask import Blueprint, request, render_template, redirect, session

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/comments/update/<int:comment_id>', methods=['POST'])
def update(comment_id):
    ...

@bp.route('/comments/delete/<int:comment_id>', methods=['POST'])
def delete(comment_id):
    ...
