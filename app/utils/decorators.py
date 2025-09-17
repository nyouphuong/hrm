from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(permission_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return abort(401)
            if current_user.role is None:
                return abort(403)
            permissions = [p.name for p in current_user.role.permissions]
            if permission_name not in permissions:
                return abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
