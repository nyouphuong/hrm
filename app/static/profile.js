function profileModal() {
    return {
        date_of_birth: '{{ current_user.date_of_birth or "" }}',
        gender: '{{ current_user.gender or "" }}',
        avatarPreview: '{{ current_user.avatar or "/static/default_avatar.png" }}',
        avatarFile: null,

        previewAvatar(event) {
            const file = event.target.files[0];
            if(file){
                this.avatarFile = file;
                this.avatarPreview = URL.createObjectURL(file);
            }
        },

        saveProfile() {
            const formData = new FormData();
            formData.append('date_of_birth', this.date_of_birth);
            formData.append('gender', this.gender);
            if(this.avatarFile) formData.append('avatar', this.avatarFile);

            fetch('/profile/update', {
                method: 'POST',
                body: formData
            }).then(res => res.json())
              .then(data => {
                  if(data.success){
                      alert('Cập nhật thành công');
                      location.reload(); // reload để cập nhật avatar
                  } else {
                      alert('Có lỗi xảy ra');
                  }
              });
        }
    }
}

