from flask import Flask, render_template, request, session
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
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    rank = db.Column(db.String(1))
    gender = db.Column(db.String(1))
    bio = db.Column(db.String(500))
    team = db.Column(db.String(25))

    def __init__(self, name, username, password, email, rank, gender, bio, team):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.rank = rank
        self.gender = gender
        self.bio = bio
        self.team = team

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return "<p>Working.</p>"
    return render_template("login.html")

@app.route("/create_account", methods=['POST', 'GET'])
def create_account():
    if request.method == "POST":
        pass
    return render_template('create_account.html')

db.create_all()
app.run('0.0.0.0', port=8000, debug=True)
