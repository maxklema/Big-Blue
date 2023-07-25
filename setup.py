from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_socketio import SocketIO
from datetime import timedelta, datetime
from werkzeug.utils import secure_filename
from datetime import datetime
import string
import hashingalg
import random
import json
import os
import sqlite3
import emails1
import sys
import re # THIS IS REGEX
import ast
from random import randint
from scoring import Scoring

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "max"
app.permanent_session_lifetime = timedelta(minutes=720)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webdata.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'static/logo_graphics/user_photos'
SCORING_FOLDER = 'static/score_files'
ALLOWED_EXTENSIONS = {'png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SCORING_FOLDER'] = SCORING_FOLDER
characters = list(string.digits)

db = SQLAlchemy(app)

class match_archive(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    filename = db.Column(db.String)
    date_added = db.Column()

    def __init__(self, username, filename, date_added):
        self.username = username
        self.filename = filename
        self.date_added = date_added

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    rank = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    bio = db.Column(db.String(500))
    team = db.Column(db.String(25))
    verified = db.Column(db.Integer)
    pic = db.Column(db.String)
    banner = db.Column(db.String)
    first_login = db.Column(db.DateTime, default="2022-06-03 03:15:12.433675")
    last_login = db.Column(db.DateTime, default="2022-06-03 03:15:12.433675")
    favored_courses = db.Column(db.String)

    def __init__(self, name, username, password, email, rank, gender, bio, team, verified, pic, banner, first_login, last_login, favored_courses):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.rank = rank
        self.gender = gender
        self.bio = bio
        self.team = team
        self.verified = verified
        self.pic = pic
        self.banner = banner
        self.first_login = first_login
        self.last_login = last_login
        self.favored_courses = favored_courses

class course(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    course_holes = db.Column(db.String(3))
    course_rating = db.Column(db.Float)
    slope_rating = db.Column(db.Float)
    par1 = db.Column(db.Integer)
    handicap1 = db.Column(db.Integer)
    par2 = db.Column(db.Integer)
    handicap2 = db.Column(db.Integer)
    par3 = db.Column(db.Integer)
    handicap3 = db.Column(db.Integer)
    par4 = db.Column(db.Integer)
    handicap4 = db.Column(db.Integer)
    par5 = db.Column(db.Integer)
    handicap5 = db.Column(db.Integer)
    par6 = db.Column(db.Integer)
    handicap6 = db.Column(db.Integer)
    par7 = db.Column(db.Integer)
    handicap7 = db.Column(db.Integer)
    par8 = db.Column(db.Integer)
    handicap8 = db.Column(db.Integer)
    par9 = db.Column(db.Integer)
    handicap9 = db.Column(db.Integer)
    par10 = db.Column(db.Integer)
    handicap10 = db.Column(db.Integer)
    par11 = db.Column(db.Integer)
    handicap11 = db.Column(db.Integer)
    par12 = db.Column(db.Integer)
    handicap12 = db.Column(db.Integer)
    par13 = db.Column(db.Integer)
    handicap13 = db.Column(db.Integer)
    par14 = db.Column(db.Integer)
    handicap14 = db.Column(db.Integer)
    par15 = db.Column(db.Integer)
    handicap15 = db.Column(db.Integer)
    par16 = db.Column(db.Integer)
    handicap16 = db.Column(db.Integer)
    par17 = db.Column(db.Integer)
    handicap17 = db.Column(db.Integer)
    par18 = db.Column(db.Integer)
    handicap18 = db.Column(db.Integer)
    city = db.Column(db.String)
    course_bio = db.Column(db.String(1000))
    created_by = db.Column(db.String)

    def __init__(self, course_name, course_holes, course_rating, slope_rating, par1, handicap1, par2, handicap2, par3, handicap3, par4, handicap4, par5, handicap5, par6, handicap6, par7, handicap7, par8, handicap8, par9, handicap9, par10, handicap10, par11, handicap11, par12, handicap12, par13, handicap13, par14, handicap14, par15, handicap15, par16, handicap16, par17, handicap17, par18, handicap18, city, course_bio, created_by):
        self.course_name = course_name
        self.course_holes = course_holes
        self.course_rating = course_rating
        self.slope_rating = slope_rating
        self.par1 = par1
        self.handicap1 = handicap1
        self.par2 = par2
        self.handicap2 = handicap2
        self.par3 = par3
        self.handicap3 = handicap3
        self.par4 = par4
        self.handicap4 = handicap4
        self.par5 = par5
        self.handicap5 = handicap5
        self.par6 = par6
        self.handicap6 = handicap6
        self.par7 = par7
        self.handicap7 = handicap7
        self.par8 = par8
        self.handicap8 = handicap8
        self.par9 = par9
        self.handicap9 = handicap9
        self.par10 = par10
        self.handicap10 = handicap10
        self.par11 = par11
        self.handicap11 = handicap11
        self.par12 = par12
        self.handicap12 = handicap12
        self.par13 = par13
        self.handicap13 = handicap13
        self.par14 = par14
        self.handicap14 = handicap14
        self.par15 = par15
        self.handicap15 = handicap15
        self.par16 = par16
        self.handicap16 = handicap16
        self.par17 = par17
        self.handicap17 = handicap17
        self.par18 = par18
        self.handicap18 = handicap18
        self.city = city
        self.course_bio = course_bio
        self.created_by = created_by

class match(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    match_name = db.Column(db.String(50))
    match_course = db.Column(db.String(50))
    event_type = db.Column(db.String(1))
    match_type = db.Column(db.String(25))
    start_time = db.Column(db.String(25))
    end_time = db.Column(db.String(25))
    teams1 = db.Column(db.String())
    total_players = db.Column(db.Integer)
    scores_file = db.Column(db.String(50))
    match_code = db.Column(db.String(6))
    match_password = db.Column(db.String())
    created_by = db.Column(db.String())
    match_live = db.Column(db.Integer, default=0)

    def __init__(self, match_name, match_course, start_time, end_time, teams1, scores_file, match_code, match_password, event_type, match_type, total_players, created_by, match_live):
        self.match_name = match_name
        self.match_course = match_course
        self.start_time = start_time
        self.end_time = end_time
        self.teams1 = teams1
        self.scores_file = scores_file
        self.match_code = match_code
        self.match_password = match_password
        self.event_type = event_type
        self.match_type = match_type
        self.total_players = total_players
        self.created_by = created_by
        self.match_live = match_live

def string_to_list(string: str) -> list:
    thing = ast.literal_eval(""+string+"")
    return thing

from course import New_Courses
from course_routes import *