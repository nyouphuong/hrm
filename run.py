from functools import wraps

from flask import abort
from flask_login import current_user

from app import create_app
from flask_socketio import SocketIO, send

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")  # thêm dòng này

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)  # đổi app.run thành socketio.run
