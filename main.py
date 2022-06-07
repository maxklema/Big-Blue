from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "max"
app.permanent_session_lifetime = timedelta(minutes=60)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    rank = db.Column(db.String(2))

    def __init__(self, name, email, rank):
        self.name = name
        self.email = email
        self.rank = rank

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "<p>Working.</p>"
    return render_template("login.html")

db.create_all()
app.run('0.0.0.0', port=8000)