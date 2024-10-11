from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home of bao"
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201
@app.route("/get-user/<userID>")
def get_user(userID):
    user = {
        "userID": userID,
        "name": "Last First",
        "email": "dummy@gmail.com"
    }
    extras = request.args.get("extras")
    if extras:
        user["extras"] = extras
    return jsonify(user),200

if __name__ == "__main__":
    app.run(debug=True)
