from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('/index.html')

@socketio.on('connect', namespace='/test')
def handle_connect():
    emit('resp', {'data': 'Connected'})

@socketio.on("PING", namespace='/test')
def handle_ping():
    emit("PONG")

if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True)

