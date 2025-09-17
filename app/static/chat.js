// static/chat.js
const socket = io();
const chatBox = document.getElementById("chat-box");
const chatMessages = document.getElementById("chat-messages");
const chatInput = document.getElementById("chat-input");
const chatSend = document.getElementById("chat-send");
const chatClose = document.getElementById("chat-close");

// Gửi username lên server khi load
const myUsername = document.getElementById("current-username").value; // hidden input
socket.emit("register", {username: myUsername});

// Gửi tin nhắn riêng
chatSend.addEventListener("click", () => {
    const msg = chatInput.value.trim();
    const recipient = document.getElementById("chat-recipient").value; // input/select
    if (msg !== "" && recipient !== "") {
        socket.emit("private_message", {sender: myUsername, recipient: recipient, message: msg});
        addMessage("You", msg);
        chatInput.value = "";
    }
});

// Nhận tin nhắn riêng
socket.on("new_private_message", (data) => {
    addMessage(data.sender, data.message);
});

function addMessage(sender, msg) {
    const div = document.createElement("div");
    div.classList.add("mb-2");
    div.innerHTML = `<span class="bg-${sender==="You"?"blue-200":"gray-200"} px-3 py-1 rounded inline-block"><b>${sender}:</b> ${msg}</span>`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Đóng chat box
chatClose.addEventListener("click", () => chatBox.style.display="none");
