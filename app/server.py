
import os, json, threading, datetime
from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_socketio import SocketIO
from dotenv import load_dotenv

load_dotenv()
DATA_PATH=os.path.join(os.path.dirname(__file__),'..','data','picnic_data.json')
_lock=threading.Lock(); presence={}

def read():
    with open(DATA_PATH,'r',encoding='utf-8') as f: return json.load(f)
def write(d):
    tmp=DATA_PATH+'.tmp'
    with open(tmp,'w',encoding='utf-8') as f: json.dump(d,f,ensure_ascii=False,indent=2)
    os.replace(tmp,DATA_PATH)

def create_app():
    app=Flask(__name__,template_folder='templates',static_folder='static')
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY','dev')
    app.config['MAX_USERS']=int(os.getenv('MAX_USERS','50'))
    return app

app=create_app()
# Use gevent async mode instead of eventlet
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='gevent')

@app.get('/')
def home(): return render_template('index.html')

@app.get('/manifest.webmanifest')
def mani(): return send_from_directory('static','manifest.webmanifest',mimetype='application/manifest+json')

@app.get('/sw.js')
def sw(): return send_from_directory('static','sw.js',mimetype='application/javascript')

if __name__=='__main__':
    port=int(os.environ.get('PORT',8000))
    socketio.run(app,host='0.0.0.0',port=port)

from flask_socketio import SocketIO
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    socketio.run(app, host='0.0.0.0', port=port)


from flask_socketio import SocketIO
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    socketio.run(app, host='0.0.0.0', port=port)



