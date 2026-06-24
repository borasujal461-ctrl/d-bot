from flask import Flask, send_file, jsonify
import json
import os

app = Flask(__name__)

COUNTER_FILE = "views.json"


def load_views():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return json.load(f)

    return {"views": 0}


def save_views(data):
    with open(COUNTER_FILE, "w") as f:
        json.dump(data, f)


@app.route("/")
def home():
    return "Flask app is running."


@app.route("/image")
def image():
    data = load_views()
    data["views"] += 1
    save_views(data)

    return send_file("photo.jpg")


@app.route("/stats")
def stats():
    return jsonify(load_views())


# PythonAnywhere imports this object directly.
# Do NOT call app.run() here.
