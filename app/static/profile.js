function userModal() {
    return {
        show: false,
        userId: null,
        username: '',
        email: '',
        role: '',
        modalTitle: 'Add User',

        // Mở modal
        openModal(id=null, username='', email='', role='') {
            this.userId = id;
            this.username = username;
            this.email = email;
            this.role = role;
            this.modalTitle = id ? 'Edit User' : 'Add User';
            this.show = true;
        },

        // Lưu (add hoặc update)
        async save() {
            try {
                const url = '/api/profile_bp/profile/update'; // endpoint update/add
                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        id: this.userId,
                        username: this.username,
                        email: this.email,
                        role: this.role
                    })
                });

                const data = await res.json();
                if (data.success) {
                    alert(this.userId ? 'User updated successfully' : 'User added successfully');
                    window.location.reload(); // reload bảng để cập nhật dữ liệu
                } else {
                    alert('Error: ' + (data.msg || 'Unknown error'));
                }
            } catch (err) {
                console.error(err);
                alert('Error saving user');
            } finally {
                this.show = false;
            }
        },

        // Xóa user
        async deleteUser() {
            if (!this.userId) return;
            if (!confirm('Are you sure to delete this user?')) return;
            try {
                const res = await fetch(`/api/profile_bp/profile/delete/${this.userId}`, {
                    method: 'POST'
                });
                const data = await res.json();
                if (data.success) {
                    alert('User deleted successfully');
                    window.location.reload();
                } else {
                    alert('Error deleting user');
                }
            } catch (err) {
                console.error(err);
                alert('Error deleting user');
            } finally {
                this.show = false;
            }
        }
    }
}
