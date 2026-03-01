from asgiref.wsgi import WsgiToAsgi
from app import app

# Expose ASGI application for Gunicorn+Uvicorn workers
asgi_app = WsgiToAsgi(app)
