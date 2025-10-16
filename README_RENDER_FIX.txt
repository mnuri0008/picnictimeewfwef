
README — Render Start Command Fix

Sorun: Log'da 'Running gunicorn app:app' görünüyor ve 'Failed to find attribute app in app' hatası alıyorsun.
Sebep: Start Command yanlış. Doğrusu, modül yolu 'app.server:app' olmalı.

İki sağlam seçenekten birini kullan:

A) Render Start Command (önerilen):
   gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT app.server:app

B) Alternatif (bu paketteki wsgi.py ile):
   gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT wsgi:app

Adımlar:
1) Bu ZIP içeriğini repo KÖKÜNE koy (wsgi.py + render.yaml).
2) Render'da:
   - Start Command'ı A veya B'deki gibi ayarla.
   - Manual Deploy → Clear build cache & deploy yap.
3) requirements.txt içinde şunlar olmalı:
   Flask==3.0.3
   Flask-SocketIO==5.3.6
   python-dotenv==1.0.1
   eventlet==0.33.3
   gunicorn==23.0.0

Not:
- Dil/SocketIO için app/server.py içinde 'app' isimli Flask uygulaması olmalı.
- Lokal çalıştırma eskisi gibi: python -m app.server
