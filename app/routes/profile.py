from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_bp = Blueprint('profile', __name__, template_folder='templates')

# Route mới để load vào iframe dashboard
@profile_bp.route('/profile/content')
@login_required
def view_content():
    return render_template('profile_content.html', current_user=current_user)
