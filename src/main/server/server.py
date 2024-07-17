import os
import json
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.main.routes import user_routes_bp
from src.main.docs import swagger_ui_blueprint

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=3)
jwt = JWTManager(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "100 per hour"],
    storage_uri="redis://localhost:6379",
)

app.register_blueprint(user_routes_bp)
app.register_blueprint(swagger_ui_blueprint)


@app.route("/swagger.json")
def swagger():
    """Load swagger.json"""

    with open("src/assets/swagger.json", "r", encoding="utf-8") as f:
        return jsonify(json.load(f))
