// sidebar.js

// Load nội dung vào iframe chính
function loadMainContent(url) {
    const iframe = document.getElementById('main-frame');
    if (iframe) {
        iframe.src = url;
    }
}
