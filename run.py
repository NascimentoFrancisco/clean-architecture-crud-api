from dotenv import load_dotenv
from src.main.server import app

if __name__ == "__main__":
    load_dotenv()
    app.run(host="0.0.0.0", port=5000)
