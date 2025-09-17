const socket = io();  // kết nối Socket.IO

// Cập nhật danh sách online users
socket.on('update_users', (users) => {
    const select = document.getElementById('chat-recipient');
    select.innerHTML = '<option value="">-- Chọn người chat --</option>';
    users.forEach(user => {
        // bỏ user hiện tại
        if (user !== document.getElementById('current-username').value) {
            select.innerHTML += `<option value="${user}">${user}</option>`;
        }
    });
});

// Gửi tin nhắn
document.getElementById('chat-send').addEventListener('click', () => {
    const messageInput = document.getElementById('chat-input');
    const recipient = document.getElementById('chat-recipient').value;
    const message = messageInput.value.trim();
    if (!message) return;
    socket.emit('send_message', { recipient, message });
    messageInput.value = '';
});

// Nhận tin nhắn
socket.on('receive_message', (data) => {
    const chatMessages = document.getElementById('chat-messages');
    const msgDiv = document.createElement('div');
    msgDiv.className = 'mb-2';
    msgDiv.innerHTML = `<strong>${data.sender}:</strong> ${data.message}`;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
});
