document.addEventListener('DOMContentLoaded', () => {
    const avatarBtn = document.getElementById('avatar-btn');
    const avatarMenu = document.getElementById('avatar-menu');

    if (!avatarBtn || !avatarMenu) return;

    // click avatar toggle menu
    avatarBtn.addEventListener('click', (e) => {
        e.stopPropagation(); // tránh bị click document ẩn luôn
        avatarMenu.classList.toggle('hidden');
    });

    // click ra ngoài sẽ ẩn menu
    document.addEventListener('click', (e) => {
        if (!avatarBtn.contains(e.target) && !avatarMenu.contains(e.target)) {
            avatarMenu.classList.add('hidden');
        }
    });
});
