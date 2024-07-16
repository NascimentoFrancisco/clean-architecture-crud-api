import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.main.routes import user_routes_bp
from src.main.docs import swagger_ui_blueprint

app = Flask(__name__)
CORS(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "100 per hour"],
    storage_uri="redis://redis:6379",
)

app.register_blueprint(user_routes_bp)
app.register_blueprint(swagger_ui_blueprint)


@app.route("/swagger.json")
def swagger():
    """Load swagger.json"""

    with open("src/assets/swagger.json", "r", encoding="utf-8") as f:
        return jsonify(json.load(f))
