from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")

@dashboard_bp.route("/dashboard")
def dashboard():
    stats = {
        "total_users": 10,
        "total_staffs": 5,
        "active_projects": 3,
    }
    return render_template("dashboard.html", stats=stats)
