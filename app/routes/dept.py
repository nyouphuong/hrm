from flask import Blueprint, render_template
from flask_login import login_required

dept_bp = Blueprint('dept', __name__, template_folder='templates')

# dữ liệu ví dụ, sau này lấy từ DB
departments = [
    {"id": 1, "name": "HR", "manager": "Alice"},
    {"id": 2, "name": "IT", "manager": "Bob"},
    {"id": 3, "name": "Finance", "manager": "Charlie"}
]

# Route content để load trong iframe dashboard
@dept_bp.route('/dept/content')
@login_required
def view_content():
    return render_template('dept_content.html', departments=departments)
