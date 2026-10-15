from flask import Flask

app = Flask(__name__)

@app.route("/api")
def home():
    return {"message": "Hello from Backend API!"}

app.run(host="0.0.0.0", port=5000)
