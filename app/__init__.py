import os
from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager, current_user
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # khi chưa login sẽ redirect tới login

    # Inject biến global vào template
    @app.context_processor
    def inject_globals():
        return dict(
            current_user=current_user,
            current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_ip=request.remote_addr
        )

    # ---------------------------
    # Register blueprints
    # ---------------------------
    from app.blueprints.dashboard import dashboard_bp
    from .routes.auth_routes import auth_bp
    from .routes.user_routes import user_bp
    from .routes.workflow_routes import workflow_bp
    from .routes.profile import profile_bp
    from .routes.dept import dept_bp
    from .routes.permission_routes import permission_bp

    app.register_blueprint(permission_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(workflow_bp, url_prefix="/api/workflow")
    app.register_blueprint(profile_bp, url_prefix="/api/profile_bp")
    app.register_blueprint(dept_bp, url_prefix="/api/dept_bp")

    # ---------------------------
    # Route gốc "/"
    # ---------------------------
    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard.dashboard"))
        return redirect(url_for("auth.login"))

    return app
