from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    server = os.environ.get("SERVER_NAME", "Unknown Server")
    return f"Hello from {server}!"

app.run(host="0.0.0.0", port=5000)
