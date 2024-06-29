from flask import jsonify
from app.db import get_recent_metrics

def init_routes(app):
    @app.route('/metrics', methods=['GET'])
    def get_metrics():
        rows = get_recent_metrics()
        return jsonify(rows)
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        return "Hello World"
