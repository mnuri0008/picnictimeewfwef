# Optional Gunicorn entrypoint — if you prefer Start Command: wsgi:app
from app.server import app  # Expose Flask app instance for Gunicorn
