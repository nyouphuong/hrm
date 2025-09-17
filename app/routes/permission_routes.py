from flask import Blueprint, render_template

permission_bp = Blueprint('permission', __name__, url_prefix='/permission')

@permission_bp.route('/')
def view_content():
    return render_template('permission.html')
