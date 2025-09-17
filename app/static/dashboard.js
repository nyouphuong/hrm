// dashboard.js

// Mapping route -> title
const titles = {
    "/profile/content": "Users",
    "/dept/content": "Departments",
    // Thêm route khác nếu cần
};

console.log("dashboard.js loaded");

// Load fragment vào main-content
function loadContent(url) {
    fetch(url)
        .then(res => res.text())
        .then(html => {
            const container = document.getElementById('main-content');
            container.innerHTML = html;

            // Re-init Alpine cho các component vừa load
//            Alpine.discoverUninitializedComponents(container)
//                 .forEach(el => Alpine.initializeComponent(el));

            // Cập nhật title
            const parser = document.createElement("a");
            parser.href = url;
            const path = parser.pathname;

            const title = titles[path] || "Dashboard";
            document.title = title;

            const headerTitle = document.querySelector("#header-title");
            if (headerTitle) headerTitle.textContent = title;
        })
        .catch(err => console.error("Error loading content:", err));
}

// Load fragment đầu tiên khi mở dashboard
document.addEventListener("DOMContentLoaded", () => {
    const defaultUrl = '/profile/content'; // hoặc '{{ url_for('profile.view_content') }}' nếu Jinja2
    loadContent(defaultUrl);
});

// Sidebar click events (nếu muốn dùng JS thay vì Alpine inline)
document.querySelectorAll("nav a").forEach(a => {
    a.addEventListener("click", e => {
        e.preventDefault();
        const url = a.getAttribute("href");
        loadContent(url);
    });
});
