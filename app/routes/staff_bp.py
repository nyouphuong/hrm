# app/staff_bp.py
from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models.department import Department
from app.models.staff import Staff

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

# ==================== VIEW ====================
@staff_bp.route('/view')
def view_content():
    staffs = Staff.query.all()
    departments = Department.query.all()
    return render_template('staff_content.html', staffs=staffs, departments=departments)

# ==================== API: ADD / UPDATE ====================
@staff_bp.route('/api/update', methods=['POST'])
def update_staff():
    data = request.get_json()
    staff_id = data.get('id')

    if staff_id:  # Update
        staff = Staff.query.get(staff_id)
        if not staff:
            return jsonify({'success': False, 'msg': 'Staff not found'})
    else:  # Add new
        staff = Staff()
        db.session.add(staff)

    staff.first_name = data.get('first_name')
    staff.last_name = data.get('last_name')
    staff.email = data.get('email')
    staff.avatar = data.get('avatar')
    staff.gender = data.get('gender')
    staff.date_of_birth = data.get('date_of_birth')
    staff.position = data.get('position')
    staff.department_id = data.get('department_id')
    staff.status = data.get('status', 'Active')

    db.session.commit()
    return jsonify({'success': True})

# ==================== API: DELETE ====================
@staff_bp.route('/api/delete/<int:id>', methods=['POST'])
def delete_staff(id):
    staff = Staff.query.get(id)
    if not staff:
        return jsonify({'success': False, 'msg': 'Staff not found'})
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'success': True})
