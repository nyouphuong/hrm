from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")

# Lưu mapping giữa username và session id
users = {}

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("connect")
def handle_connect():
    print("User connected")

@socketio.on("register")
def handle_register(data):
    username = data["username"]
    users[username] = request.sid  # gán socket id cho username
    print(f"{username} đăng nhập với sid {request.sid}")

@socketio.on("private_message")
def handle_private_message(data):
    sender = data["sender"]
    recipient = data["recipient"]
    message = data["message"]

    if recipient in users:  # nếu user đang online
        recipient_sid = users[recipient]
        emit("new_private_message",
             {"sender": sender, "message": message},
             room=recipient_sid)

if __name__ == "__main__":
    socketio.run(app, debug=True)
