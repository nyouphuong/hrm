import os

from flask import Blueprint, render_template, request, jsonify, current_app
from flask_login import login_required, current_user
from app import db
from ..models import User  # đảm bảo import model User

profile_bp = Blueprint('profile', __name__, template_folder='templates')

# Route load content
@profile_bp.route('/profile/content')
@login_required
def view_content():
    users = User.query.all()  # load tất cả user để hiển thị table
    return render_template('profile_content.html', users=users, current_user=current_user)

@profile_bp.route('/api/users', methods=['GET'])
@login_required
def get_all_users():
    users = User.query.all()
    user_list = [{'username': u.username, 'avatar': u.avatar} for u in users]
    return jsonify(user_list)

@profile_bp.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    date_of_birth = request.form.get('date_of_birth')
    gender = request.form.get('gender')

    if date_of_birth:
        current_user.date_of_birth = date_of_birth
    if gender:
        current_user.gender = gender

    if 'avatar' in request.files:
        file = request.files['avatar']
        if file.filename:
            from werkzeug.utils import secure_filename
            filename = secure_filename(f"{current_user.id}{os.path.splitext(file.filename)[1]}")
            upload_folder = os.path.join(current_app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            current_user.avatar = f'/static/uploads/{filename}'

    db.session.commit()
    return jsonify({'success': True})

