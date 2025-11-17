from flask import Flask, request, jsonify
from flask_cors import CORS
import kociemba
import os   # <-- REQUIRED

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"status": "Cube Solver API Running"}

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()

    if 'cube' not in data:
        return jsonify({"error": "cube field missing"}), 400

    cube_string = data['cube']

    try:
        solution = kociemba.solve(cube_string)
        return jsonify({"solution": solution, "status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 400


# 🔥 REQUIRED FOR RENDER
if __name__ == '__main__':
    print("Starting Flask server...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
