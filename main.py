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

        username_input = request.form['username']
        password_input = request.form['password']
        found_user = users.query.filter_by(username=username_input).first()
        
        if found_user and found_user.username == username_input and found_user.password == password_input:
            return "<p>Working.</p>"
        else:
            return "<p>Sorry. That is incorect.</p>"

    return render_template("login.html")

@app.route("/create_account", methods=['POST', 'GET'])
def create_account():
    if request.method == "POST":

        for item in request.form:
            if request.form[item] == "":
                return "<p>Please input all correct values.</p>"
    
        new_user = users(request.form['name'], request.form['username'], request.form['password'], request.form['email'], request.form['rank'], request.form['gender'], request.form['bio'], request.form['team'])
        db.session.add(new_user)
        db.session.commit()

        return render_template('create_account.html', message="Account created sucessfully!")

    return render_template('create_account.html')

db.create_all()
app.run('0.0.0.0', port=8000, debug=True)
