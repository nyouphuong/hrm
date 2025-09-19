from .. import db
from datetime import datetime


class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(255))  # lưu path ảnh
    gender = db.Column(db.String(10))   # Male / Female / Other
    date_of_birth = db.Column(db.Date)
    position = db.Column(db.String(100))  # Chức vụ
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Active')  # Active / Inactive

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Staff {self.full_name()}>"

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'full_name': self.full_name,
            'department': self.department,
            'position': self.position,
        }
