from app import create_app
from flask_socketio import SocketIO, send

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")  # thêm dòng này

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)  # đổi app.run thành socketio.run
