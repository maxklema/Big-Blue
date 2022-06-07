from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "<p>Working.</p>"
    return render_template("login.html")

app.run('0.0.0.0', port=8000)