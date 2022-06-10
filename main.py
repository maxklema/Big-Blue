from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, inspect
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

class course(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    pars_of_holes = db.Column(db.String)
    course_stats = db.Column(db.String(1000))

    def __init__(self, course_name, pars_of_holes, course_stats):
        self.course_name = course_name
        self.pars_of_holes = pars_of_holes
        self.course_stats = course_stats

class match(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    match_name = db.Column(db.String(50))
    match_course = db.Column(db.String(50))
    start_time = db.Column(db.String(25))
    end_time = db.Column(db.String(25))
    participating_teams = (db.String(500))
    scores_file = (db.String(50))

    def __init__(self, match_name, match_course, start_time, end_time, participating_teams, scores_file):
        self.match_name = match_name
        self.match_course = match_course
        self.start_time = start_time
        self.end_time = end_time
        self.participating_teams = participating_teams
        self.scores_file = scores_file

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/header", methods=['GET'])
def header():
    return render_template("header.html")

@app.route("/error/<msg>")
def error(msg):
    return render_template("error.html", message=msg)


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

@app.route("/return_user_data/<password>", methods=['GET'])
def return_user_data(password):
    if password == "123":
        list_of_users = users.query.all()
        dict_to_send = {}
        for item in list_of_users:
            dict_to_send[item._id] = object_as_dict(item)
        return dict_to_send,200
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

db.create_all()
app.run('0.0.0.0', port=8000, debug=True)
