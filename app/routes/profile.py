from flask import Blueprint, render_template, request, jsonify
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

# Route update user qua AJAX
@profile_bp.route('/profile/update', methods=['POST'])
@login_required
def update_user():
    data = request.json
    user_id = data.get('id')
    username = data.get('username')
    email = data.get('email')
    role = data.get('role')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'success': False, 'msg': 'User not found'}), 404

    user.username = username
    user.email = email
    user.role = role
    db.session.commit()

    return jsonify({'success': True, 'msg': 'User updated successfully'})
