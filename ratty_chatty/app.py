import os

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-noes-secrets!"
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('index.html')

@socketio.on('message')
def handle_message(data):
  print(f"received message: {data}")

def run():
  os.environ['FLASK_ENV'] = "development"
  socketio.run(app, "0.0.0.0", debug=True)
