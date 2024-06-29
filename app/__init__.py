from flask import Flask
from app.routes import init_routes
from app.db import init_db

def create_app():
    app = Flask(__name__)
    init_db()
    init_routes(app)
    return app
