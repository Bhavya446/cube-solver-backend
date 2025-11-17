from flask import Flask, request, jsonify
import kociemba

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "Cube solver API running"}), 200

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json() or {}
    cube = data.get("cube")

    if not cube:
        return jsonify({"error": "Request JSON must include 'cube' field"}), 400

    try:
        # cube is the 54-character facelet string like "UUUUUU...BBBBBBB"
        solution = kociemba.solve(cube)
        return jsonify({
            "solution": solution,
            "status": "ok",
        }), 200
    except Exception as e:
        # Any error in the cube string or solver
        return jsonify({
            "status": "error",
            "error": str(e),
        }), 400


if __name__ == "__main__":
    # local testing (optional)
    app.run(host="0.0.0.0", port=5000, debug=True)
