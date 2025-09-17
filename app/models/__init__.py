from .. import db


# Import models here so alembic / flask-migrate can detect them
from .user import User
from .staff import Staff
from .department import Department

