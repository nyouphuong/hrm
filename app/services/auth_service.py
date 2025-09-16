import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask import current_app


class AuthService:
    @staticmethod
    def hash_password(raw_password: str) -> str:
        return generate_password_hash(raw_password)

    @staticmethod
    def verify_password(hash_pw: str, raw_password: str) -> bool:
        return check_password_hash(hash_pw, raw_password)

    @staticmethod
    def authenticate(username, password):
        from ..models.user import User
        user = User.query.filter_by(username=username).first()
        if not user:
            return None
        if not AuthService.verify_password(user.password_hash, password):
            return None

        payload = {
            'sub': user.id,
            'exp': datetime.utcnow() + timedelta(hours=8)
        }
        token = jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm='HS256')
        return token
