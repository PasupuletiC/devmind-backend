from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/generate")
def generate():
    return jsonify({"message": "Backend working!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
