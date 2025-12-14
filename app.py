from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ✅ ROOT ROUTE (THIS FIXES 404)
@app.route("/")
def home():
    return jsonify({
        "status": "DevMind backend running",
        "message": "API is live"
    })

@app.route("/api/data")
def data():
    return jsonify({"message": "Hello from backend"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
