from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(
        "http://backend:5000/api",
        timeout=5
    )
    return f"<h1>Project 3</h1><p>{response.json()['message']}</p>"

app.run(host="0.0.0.0", port=5001)
