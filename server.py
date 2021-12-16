from flask import Flask, request
from flask_cors import CORS

from summarizer import summarizer

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST", "GET"])
def summarize():
    if request.method == "POST":
        print(request.json)
    return {"summarize": ["text"]}


if __name__ == "__main__":
    app.run(debug=True)
