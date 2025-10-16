
README_DEPLOY.txt — Render güvenli paket (Python 3.12 + eventlet)

1) Bu ZIP'teki dosyaları GitHub projenizin KÖK dizinine kopyalayın/üzerine yazın:
   - runtime.txt   -> Render Python sürümünü 3.12.6 olarak sabitler
   - requirements.txt -> eventlet + gunicorn içerir (3.12 ile uyumlu)

2) app/server.py dosyanızı aşağıdaki gibi ayarlayın (kritik satırlar):
   ------------------------------------------------------------------
   from flask_socketio import SocketIO

   # Flask app'i oluşturduktan sonra:
   socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

   if __name__ == '__main__':
       import os
       port = int(os.environ.get('PORT', 8000))
       socketio.run(app, host='0.0.0.0', port=port)
   ------------------------------------------------------------------

3) Render panelinde Start Command:
   gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT app.server:app

4) Render’da "Manual Deploy → Clear build cache & deploy" yapın.

Not:
- Eğer repo kökünde değil de alt klasörde iseniz Render "Root Directory" alanına
  o klasörün adını girin (örn. `nuri_piknik_v5_final`).
- Bu paket Python 3.13 kaynaklı gevent/eventlet derleme problemlerini
  atlamak için Python'ı 3.12'ye sabitler. Bu kombinasyon Render'da stabil çalışır.
