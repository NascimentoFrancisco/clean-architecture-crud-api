import json
from flask import Flask, jsonify
from flask_cors import CORS
from src.main.routes import user_routes_bp
from src.main.docs import swagger_ui_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(user_routes_bp)
app.register_blueprint(swagger_ui_blueprint)


@app.route("/swagger.json")
def swagger():
    """Load swagger.json"""

    with open("src/assets/swagger.json", "r", encoding="utf-8") as f:
        return jsonify(json.load(f))
