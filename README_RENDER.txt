
NURI • Render Ready (Final)

Bu paketi GitHub repo KÖK klasörüne koyun ve deploy edin.
İçerik:
- runtime.txt          -> Python 3.12.6 (Render'da stabil)
- requirements.txt     -> Flask + Flask-SocketIO + eventlet + gunicorn
- render.yaml          -> Doğru build/start komutları (tek tık Blueprint)
- wsgi.py              -> (Opsiyonel) Start Command'ı 'wsgi:app' kullanmak isterseniz

Render ayarları:
- Build Command : pip install -r requirements.txt
- Start Command : gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT app.server:app
  (Alternatif)   : gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT wsgi:app
- Env Vars      : SECRET_KEY=nuri-prod-secret-change-me , MAX_USERS=50

app/server.py içinde bulunduğundan emin olun:
from flask_socketio import SocketIO
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    socketio.run(app, host='0.0.0.0', port=port)

Deploy adımları:
1) Bu dosyaları repo köküne ekleyip push edin.
2) Render: Manual Deploy -> Clear build cache & deploy.
3) Dilerseniz render.yaml ile "New + From Blueprint" de yapabilirsiniz.
