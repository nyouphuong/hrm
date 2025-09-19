let currentPage = 'profile';

function loadContent(url, page) {
    currentPage = page;

    fetch(url)
        .then(res => res.text())
        .then(html => {
            document.getElementById("main-content").innerHTML = html;

            const newBtn = document.getElementById("new-btn");
            const saveBtn = document.getElementById("save-btn");

            // Ẩn trước
            newBtn.classList.add("hidden");
            saveBtn.classList.add("hidden");

            // Hiện nút theo page
            switch(page) {
                case 'profile':
                    saveBtn.classList.remove("hidden");   // chỉ Save
                    break;
                case 'dept':
                    newBtn.classList.remove("hidden");    // chỉ New
                    break;
                case 'staff':
                    newBtn.classList.remove("hidden");
                    saveBtn.classList.remove("hidden");   // cả hai
                    break;
                case 'permission':
                    saveBtn.classList.remove("hidden");   // chỉ Save
                    break;
            }
        })
        .catch(err => console.error(err));
}

// Save tổng quát: tự tìm form trong #main-content
document.getElementById("save-btn").addEventListener("click", () => {
    const mainContent = document.getElementById("main-content");
    const form = mainContent.querySelector("form");

    if(!form) {
        alert("Không có form để lưu!");
        return;
    }

    const method = (form.method || "POST").toUpperCase();
    const formData = new FormData(form);

    if(method === "GET") {
        // GET không thể có body, append vào query string
        const params = new URLSearchParams(formData).toString();
        fetch(form.action + "?" + params, { method: "GET" })
            .then(res => res.text())
            .then(html => {
                document.getElementById("main-content").innerHTML = html;
                alert("Lưu thành công!");
            })
            .catch(err => console.error(err));
    } else {
        // POST hoặc khác
        fetch(form.action, { method: method, body: formData })
            .then(res => res.text())
            .then(html => {
                document.getElementById("main-content").innerHTML = html;
                alert("Lưu thành công!");
            })
            .catch(err => console.error(err));
    }
});

// Load fragment đầu tiên khi mở dashboard
document.addEventListener("DOMContentLoaded", () => {
    const defaultUrl = '{{ url_for("profile.view_content") }}'; // Flask phải render
    loadContent(defaultUrl, 'profile');
});

// Sidebar click events
document.querySelectorAll("nav a").forEach(a => {
    a.addEventListener("click", e => {
        e.preventDefault();
        const url = a.getAttribute("href");
        const page = a.getAttribute("data-page"); // cần thêm data-page="profile"/"dept"
        loadContent(url, page);
    });
});
