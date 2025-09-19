function staffModal() {
    return {
        show: false,
        showNewButton: true,
        staffId: null,
        modalTitle: 'Add Staff',
        first_name: '',
        last_name: '',
        email: '',
        position: '',
        department_id: '',
        gender: '',
        date_of_birth: '',
        status: 'Active',

        openModal(id=null, first_name='', last_name='', email='', position='', department_id=null, avatar='', gender='', date_of_birth='', status='Active') {
            this.staffId = id;
            this.first_name = first_name;
            this.last_name = last_name;
            this.email = email;
            this.position = position;
            this.department_id = department_id;
            this.gender = gender;
            this.date_of_birth = date_of_birth;
            this.status = status;
            this.modalTitle = id ? 'Edit Staff' : 'Add Staff';
            this.show = true;
        },

        async save() {
            try {
                const url = '/staff/api/update';
                const res = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        id: this.staffId,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        email: this.email,
                        position: this.position,
                        department_id: this.department_id,
                        gender: this.gender,
                        date_of_birth: this.date_of_birth,
                        status: this.status
                    })
                });
                const data = await res.json();
                if (data.success) {
                    alert(this.staffId ? 'Staff updated successfully' : 'Staff added successfully');
                    window.location.reload();
                } else {
                    alert('Error: ' + (data.msg || 'Unknown error'));
                }
            } catch (err) {
                console.error(err);
                alert('Error saving staff');
            } finally {
                this.show = false;
            }
        },

        async deleteStaff() {
            if (!this.staffId) return;
            if (!confirm('Are you sure to delete this staff?')) return;
            try {
                const res = await fetch(`/staff/api/delete/${this.staffId}`, { method: 'POST' });
                const data = await res.json();
                if (data.success) {
                    alert('Staff deleted successfully');
                    window.location.reload();
                } else {
                    alert('Error deleting staff');
                }
            } catch (err) {
                console.error(err);
                alert('Error deleting staff');
            } finally {
                this.show = false;
            }
        }
    }
}
