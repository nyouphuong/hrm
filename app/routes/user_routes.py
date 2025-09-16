from flask import Blueprint, jsonify
from ..models.user import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])
