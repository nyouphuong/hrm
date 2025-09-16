import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://hrm:P%40ssw0rdA@localhost:5432/hrm'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    JWT_SECRET = os.getenv('JWT_SECRET', 'jwt-secret')
