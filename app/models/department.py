from .. import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)  # Mã bộ phận
    name = db.Column(db.String(100), nullable=False)             # Tên bộ phận

    def __repr__(self):
        return f"<Department {self.code} - {self.name}>"
