
NURI PIKNIK v5 FINAL - KURULUM (Windows)

1) ZIP'i bir klasöre çıkarın. Örnek yol:
   C:\Users\navigator\Desktop\nuri_piknik_v5_final

2) PowerShell açın ve klasöre geçin:
   cd "C:\Users\navigator\Desktop\nuri_piknik_v5_final"

3) Geçici olarak script izni verin:
   Set-ExecutionPolicy -Scope Process Bypass -Force

4) Uygulamayı başlatın:
   .\tools\run_local.ps1

Tarayıcı adresi: http://127.0.0.1:8000

Sorun olursa alternatif manuel başlangıç:
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe -m app.server
