from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO
from datetime import datetime
import string
import hashingalg
import random
import json
import os
import sqlite3
import sys
import re # THIS IS REGEX
from random import randint

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "max"
app.permanent_session_lifetime = timedelta(minutes=600)
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

    def __init__(self, name, username, password, email, rank, gender, bio, team, verified, pic, banner, first_login, last_login):
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

class course(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    course_holes = db.Column(db.String(3))
    par1 = db.Column(db.Integer)
    par2 = db.Column(db.Integer)
    par3 = db.Column(db.Integer)
    par4 = db.Column(db.Integer)
    par5 = db.Column(db.Integer)
    par6 = db.Column(db.Integer)
    par7 = db.Column(db.Integer)
    par8 = db.Column(db.Integer)
    par9 = db.Column(db.Integer)
    par10 = db.Column(db.Integer)
    par11 = db.Column(db.Integer)
    par12 = db.Column(db.Integer)
    par13 = db.Column(db.Integer)
    par14 = db.Column(db.Integer)
    par15 = db.Column(db.Integer)
    par16 = db.Column(db.Integer)
    par17 = db.Column(db.Integer)
    par18 = db.Column(db.Integer)
    city = db.Column(db.String)
    course_bio = db.Column(db.String(1000))
    created_by = db.Column(db.String)

    def __init__(self, course_name, course_holes, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, par17, par18, city, course_bio, created_by):
        self.course_name = course_name
        self.course_holes = course_holes
        self.par1 = par1
        self.par2 = par2
        self.par3 = par3
        self.par4 = par4
        self.par5 = par5
        self.par6 = par6
        self.par7 = par7
        self.par8 = par8
        self.par9 = par9
        self.par10 = par10
        self.par11 = par11
        self.par12 = par12
        self.par13 = par13
        self.par14 = par14
        self.par15 = par15
        self.par16 = par16
        self.par17 = par17
        self.par18 = par18
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

#Scoring class
class Scoring():
    def create_json(filename, match_code, match_password, number_holes, match_name, start_time, end_time, home_team, away_team, match_type, gamemode, Id, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, par17, par18):
        data = {"players":{}, "match_info": {"par1": par1, "par2": par2, "par3": par3, "par4": par4, "par5": par5, "par6": par6, "par7": par7, "par8": par8, "par9": par9, "par10": par10, "par11": par11, "par12": par12, "par13": par13, "par14": par14, "par15": par15, "par16": par16, "par17": par17, "par18": par18, "match_code": match_code, "match_password": match_password, "number_holes": number_holes, "match_name": match_name, "start_time": start_time, "end_time": end_time, "home_team":home_team, "away_team": away_team, "match_type": match_type, "gamemode": gamemode, "id": Id},"lobby":[], "message": ""}
        #json_string = json
        with open("static/score_files/" + str(filename) + ".json", "a+") as file:
            
            #print(json.dump(data, file, indent=3))
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def new_create_json(filename, match_code, match_password, number_holes, match_name, start_time, end_time, num_teams, teams, match_type, gamemode, Id, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, par17, par18):
        data = {"players":{}, "match_info": {"par1": par1, "par2": par2, "par3": par3, "par4": par4, "par5": par5, "par6": par6, "par7": par7, "par8": par8, "par9": par9, "par10": par10, "par11": par11, "par12": par12, "par13": par13, "par14": par14, "par15": par15, "par16": par16, "par17": par17, "par18": par18, "match_code": match_code, "match_password": match_password, "number_holes": number_holes, "match_name": match_name, "start_time": start_time, "end_time": end_time, "team_scores": {}, "match_type": match_type, "gamemode": gamemode, "id": Id},"lobby":[], "message": ""}
        for team in teams:
            data["teams"][team] = 0
        with open("static/score_files/" + str(filename) + ".json", "a+") as file:
            
            #print(json.dump(data, file, indent=3))
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def add_to_lobby(filename, player):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            data["lobby"].append(player)
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()
        
    def change_message(filename, message):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            data["message"] = str(message)
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def kick_player(filename, player):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            try:
                player = player.replace(' ', '%20')
                try:
                    del data["players"][player]
                except:
                    del data["players"][player]
            except:
                player = player.replace('%20', ' ')
                try:
                    for waiting in data["lobby"]:
                        if waiting[0] == player:
                            data["lobby"].remove(waiting)
                            break
                except: 
                    pass
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def add_player(filename, player, team):
        #json.load("test.json")
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            holes = {}
            if data["match_info"]["number_holes"] == "9":
                holes = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            elif data["match_info"]["number_holes"] == "18":
                holes = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0}
                
            data["players"][player] = {"team": team, "opponent": "","scores":holes}

            for waiting in data["lobby"]:
                if waiting[0] == player:
                    data["lobby"].remove(waiting)
                    break

            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()
    
    def change_opponent(filename, player1, player2):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            data["players"][player1]["opponent"] = player2
            data["players"][player2]["opponent"] = player1
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def edit_score(filename, player, hole, new_score): #used by both players and coaches
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            if player in data["players"]: #POSSIBLE PLACE FOR ERRORS
                data["players"][player]["scores"][str(hole)] = new_score
                print("NEW SCORE:" + new_score)
                file.seek(0)
                json_object = json.dump(data, file, indent=3)
                file.truncate()

    def calc_match_status(filename, player1, player2):
        try:
            with open("static/score_files/" + str(filename) + ".json", "r") as file:
                file.seek(0)
                data = json.load(file)
                status=""
                score=0
                first_scores = data["players"][player1]["scores"]
                second_scores = data["players"][player2]["scores"]
                last_hole=0
                for i in range(int(data["match_info"]["number_holes"])):
                    if (int(first_scores[str(i+1)]) != 0) and (int(second_scores[str(i+1)]) != 0):
                        last_hole+=1
                        if int(first_scores[str(i+1)]) < int(second_scores[str(i+1)]):
                            score+=1
                        elif int(second_scores[str(i+1)]) < int(first_scores[str(i+1)]):
                            score-=1
                    else:
                        break
                holes_left = int(data["match_info"]["number_holes"]) - last_hole
                print(score)
                if score > 0:
                    if holes_left == 0:
                        
                        status = player1 + " wins " + str(score) + " up"
                    elif score > holes_left:
                        status = player1 + " wins " + str(score) + " & " + str(holes_left)
                    else:
                        status= player1 + " up " + str(score) + " thru " + str(last_hole)
                elif score < 0:
                    if holes_left == 0:
                        
                        status = player2 + " wins " + str(abs(score)) + " up"
                    elif abs(score) > holes_left:
                        status = player2 + " wins " + str(abs(score)) + " & " + str(holes_left)
                    else:
                        status= player2 + " up " + str(abs(score)) + " thru " + str(last_hole)
                else:
                    status = "AS" + " thru " + str(last_hole)
                
                return status
        except:
            with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                status=""
                score=0
                first_scores = data["players"][player1]["scores"]
                second_scores = data["players"][player2]["scores"]
                last_hole=0
                for i in range(int(data["match_info"]["number_holes"])):
                    if (int(first_scores[str(i+1)]) != 0) and (int(second_scores[str(i+1)]) != 0):
                        print(int(first_scores[str(i+1)]), int(second_scores[str(i+1)]))
                        last_hole+=1
                        if int(first_scores[str(i+1)]) < int(second_scores[str(i+1)]):
                            score+=1
                        elif int(second_scores[str(i+1)]) < int(first_scores[str(i+1)]):
                            score-=1
                    else:
                        break
                holes_left = int(data["match_info"]["number_holes"]) - last_hole
                if score > 0:
                    if holes_left == 0:
                        
                        status = player1 + " wins " + str(score) + " up"
                    elif score > holes_left:
                        status = player1 + " wins " + str(score) + " & " + str(holes_left)
                    else:
                        status= player1 + " up " + str(score) + " thru " + str(last_hole)
                elif score < 0:
                    if holes_left == 0:
                        
                        status = player2 + " wins " + str(abs(score)) + " up"
                    elif abs(score) > holes_left:
                        status = player2 + " wins " + str(abs(score)) + " & " + str(holes_left)
                    else:
                        status= player2 + " up " + str(abs(score)) + " thru " + str(last_hole)
                else:
                    status = "AS" + " thru " + str(last_hole)
                
                return status



    def add_scores(data):
        sum = 0
        for hole in data:
            if data[hole] != "":
                sum += int(data[str(hole)])
        return sum


    def calc_match_play_results(filename):
        try:
            with open("static/score_files/" + str(filename) + ".json", "r") as file:
                file.seek(0)
                data = json.load(file)
                team1 = [data["match_info"]["home_team"], 0]
                team2 = [data["match_info"]["away_team"], 0]
                
                team1_total = 0
                team2_total = 0
                
                if int(filename) == 54:
                    team1_total = 6
                    team2_total = 4
                
                for player in data["players"]:
                    if data["players"][player]["team"] == team1[0] and data["players"][player]["opponent"] != "":
                        match_status = Scoring.calc_match_status(filename, player, data["players"][player]["opponent"])
                        if (match_status.startswith(player + " wins")):
                            team1_total += 1
                        elif (match_status.startswith(data["players"][player]["opponent"] + " wins")):
                            team2_total += 1
                        elif (match_status.startswith("AS thru " + data['match_info']['number_holes'])):
                            team1_total += 0.5
                            team2_total += 0.5

                team1[1] += team1_total
                team2[1] += team2_total


                return team1, team2
        except:
            with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                team1 = [data["match_info"]["home_team"], 0]
                team2 = [data["match_info"]["away_team"], 0]
                team1_total = 0
                team2_total = 0
                for player in data["players"]:
                    if data["players"][player]["team"] == team1[0]:
                        try:
                            match_status = Scoring.calc_match_status(filename, player, data["players"][player]["opponent"])
                            if (match_status.startswith(player + " wins")):
                                team1_total += 1
                            elif (match_status.startswith(data["players"][player]["opponent"] + " wins")):
                                team2_total += 1
                            elif (match_status.startswith("AS thru " + data['match_info']['number_holes'])):
                                team1_total += 0.5
                                team2_total += 0.5
                        except:
                            continue

                team1[1] += team1_total
                team2[1] += team2_total

                print("TEAM ONE TOTAL: " + str(team1_total))

                return team1, team2



    def calc_match_results(filename):
        try: 
            with open("static/score_files/" + str(filename) + ".json", "r") as file:
                file.seek(0)
                data = json.load(file)
                team1 = [data["match_info"]["home_team"], 0]
                team2 = [data["match_info"]["away_team"], 0]
                team1_list = []
                team2_list = []
                team1_total = 0
                team2_total = 0


                for player in data["players"].values():
                    if player["team"] == team1[0]:
                        team1_list.append(Scoring.add_scores(player['scores']))
                    elif player["team"] == team2[0]:
                        team2_list.append(Scoring.add_scores(player['scores']))
                team1_list.sort()
                team2_list.sort()
                print(team1_list, team2_list)
                for i in team1_list:
                    print(i)
                    if team1_list.index(i) <= 3:
                        print("here????")
                        team1_total += i
                for i in team2_list:
                    if team2_list.index(i) <= 3:
                        print("here????")
                        team2_total += i

                

                team1[1] += team1_total
                team2[1] += team2_total

                return team1, team2
        except:
             with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                team1 = [data["match_info"]["home_team"], 0]
                team2 = [data["match_info"]["away_team"], 0]
                team1_list = []
                team2_list = []
                team1_total = 0
                team2_total = 0


                for player in data["players"].values():
                    print(player)
                    if player["team"] == team1[0]:
                        team1_list.append(Scoring.add_scores(player['scores']))
                    elif player["team"] == team2[0]:
                        team2_list.append(Scoring.add_scores(player['scores']))
                team1_list.sort()
                team2_list.sort()
                print(team1_list, team2_list)
                for i in team1_list:
                    print(i)
                    if team1_list.index(i) <= 3:
                        print("here????")
                        team1_total += i
                        print(team1_total, team2_total)
                for i in team2_list:
                    if team2_list.index(i) <= 3:
                        print("here????")
                        team2_total += i
                        print(team1_total, team2_total)

                

                team1[1] += team1_total
                team2[1] += team2_total

                return team1, team2

    def calc_relation_to_par(filename, player):
        try:
            with open("static/score_files/" + str(filename) + ".json", "r") as file:
                file.seek(0)
                data = json.load(file)
                player_score = data["players"][player]["scores"]
                last_hole = 0
                current_score = 0
                current_par = 0
                for i in range(int(data["match_info"]["number_holes"])):
                    if (player_score[str(i+1)] != 0):
                        last_hole+=1
                        current_score += int(player_score[str(i+1)])
                        current_par += data["match_info"]["par" + str(i+1)]
                    else:
                        break
                absolute_relation = str(abs(current_score - current_par))
                if last_hole == int(data["match_info"]["number_holes"]):
                    return "F: " + str(current_score)
                elif current_score > current_par:
                    return "+" + absolute_relation + " thru " + str(last_hole)
                elif current_score < current_par:
                    return "-" + absolute_relation + " thru " + str(last_hole)
                else:
                    return "E" + " thru " + str(last_hole)
        except:
            with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                player_score = data["players"][player]["scores"]
                last_hole = 0
                current_score = 0
                current_par = 0
                for i in range(int(data["match_info"]["number_holes"])):
                    if (player_score[str(i+1)] != 0):
                        last_hole+=1
                        current_score += int(player_score[str(i+1)])
                        current_par += data["match_info"]["par" + str(i+1)]
                    else:
                        break
                absolute_relation = str(abs(current_score - current_par))
                if ((last_hole == int(data["match_info"]["number_holes"])) and (current_score < current_par)):
                    return "F: " + str(current_score) + " (-" + absolute_relation + ")"
                elif ((last_hole == int(data["match_info"]["number_holes"])) and (current_score > current_par)):
                    return "F: " + str(current_score) + " (+" + absolute_relation + ")"
                elif current_score > current_par:
                    return "+" + absolute_relation + " thru " + str(last_hole)
                elif current_score < current_par:
                    return "-" + absolute_relation + " thru " + str(last_hole)
                else:
                    return "E" + " thru " + str(last_hole)
    
    def return_data(filename):
        with open("static/score_files/" + str(filename) + ".json", "r") as file:
            file.seek(0)
            data = json.load(file)
            return data
    def return_archive_data(filename):
        with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
            file.seek(0)
            data = json.load(file)
            return data
    def get_team_scores(filename):
        try:
            teamscores = {}
            with open("static/score_files/" + str(filename) + ".json", "r") as file:
                file.seek(0)
                data = json.load(file)
                for player in data["players"].values():
                    if player["team"] in teamscores.keys():
                        teamscores[player["team"]] += Scoring.add_scores(player['scores'])
                    else:
                        teamscores[player["team"]] = 0
                        teamscores[player["team"]] += Scoring.add_scores(player['scores'])
                    
                        
                return teamscores
        except:
            teamscores = {}
            with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                for player in data["players"].values():
                    if player["team"] in teamscores.keys():
                        teamscores[player["team"]] += Scoring.add_scores(player['scores'])
                    else:
                        teamscores[player["team"]] = 0
                        teamscores[player["team"]] += Scoring.add_scores(player['scores'])
                    
                        
                return teamscores

    def get_lowest_team_score(team_scores):
        lowest_score = 2**31 - 1
        lowest_teams = []
        for team in team_scores.keys():
            if team_scores[team] < lowest_score:
                lowest_teams = [team]
                lowest_score = team_scores[team]
            elif team_scores[team] == lowest_score:
                lowest_teams.append(team)
        
        return (lowest_teams, lowest_score)

    def generate_leader_board(team_scores):
        leader_board = []
        for team in team_scores.keys():
            leader_board.append((team, team_scores[team]))
        
        for i in range(len(leader_board)):
            for j in range(0, len(leader_board) - i - 1):
                
                # Range of the leader_boarday is from 0 to n-i-1
                # Swap the elements if the element found
                #is greater than the adjacent element
                if leader_board[j][1] > leader_board[j + 1][1]:
                    leader_board[j], leader_board[j + 1] = leader_board[j + 1], leader_board[j]
        return leader_board
            

def archive_match(filename):
    with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "a+") as file:
        file.seek(0)
        json_object = json.dump(Scoring.return_data(filename), file, indent=3)
        file.truncate()

def get_archived_match(filename):
    with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
        file.seek(0)
        data = json.load(file)
        return data

def return_admin_data():
    db = sqlite3.connect('instance/webdata.sqlite3')
    data = db.execute("select * from users")
    data_dict = {}

    data_dict[0] = {"name": "Name", "username": "Username", "password": "Password", "email": "Email", "rank": "Rank", "gender": "Gender", "bio": "Bio", "team": "Team", "verified": "Verified", "pic": "Picture File"}
    
    for row in data:
        data_dict[len(data_dict)+1] = {"name": row[1], "username": row[2], "password": row[3], "email": row[4], "rank": row[5], "gender": row[6], "bio": row[7], "team": row[8], "verified": row[9], "pic": row[10]}

    return data_dict

def sanitize_inputs(string_to_analize):
    invalid_list = ['2 girls 1 cup', '2g1c', '4r5e', '5h1t', '5hit', 'a_s_s', 'a55', 'acrotomophilia', 'alabama hot pocket', 'alaskan pipeline', 'anal', 'anilingus', 'anus', 'apeshit', 'ar5e', 'arrse', 'arse', 'arsehole', 'ass', 'ass-fucker', 'ass-hat', 'ass-jabber', 'ass-pirate', 'assbag', 'assbandit', 'assbanger', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfuck', 'assfucker', 'assfukka', 'assgoblin', 'asshat', 'asshead', 'asshole', 'assholes', 'asshopper', 'assjacker', 'asslick', 'asslicker', 'assmonkey', 'assmunch', 'assmuncher', 'assnigger', 'asspirate', 'assshit', 'assshole', 'asssucker', 'asswad', 'asswhole', 'asswipe', 'auto erotic', 'autoerotic', 'axwound', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'babeland', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', 'ballbag', 'balls', 'ballsack', 'bampot', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaner', 'beaners', 'beastial', 'beastiality', 'beaver cleaver', 'beaver lips', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbos', 'birdlock', 'bitch', 'bitchass', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bitchtits', 'bitchy', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody', 'blow job', 'blow your load', 'blowjob', 'blowjobs', 'blue waffle', 'blumpkin', 'boiolas', 'bollock', 'bollocks', 'bollok', 'bollox', 'bondage', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'booty call', 'breasts', 'breeder', 'brotherfucker', 'brown showers', 'brunette action', 'buceta', 'bugger', 'bukkake', 'bulldyke', 'bullet vibe', 'bullshit', 'bum', 'bumblefuck', 'bung hole', 'bunghole', 'bunny fucker', 'busty', 'butt', 'butt plug', 'butt-pirate', 'buttcheeks', 'buttfucka', 'buttfucker', 'butthole', 'buttmuch', 'buttplug', 'c0ck', 'c0cksucker', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'cawk', 'chesticle', 'chinc', 'chink', 'choad', 'chocolate rosebuds', 'chode', 'cipa', 'circlejerk', 'cl1t', 'cleveland steamer', 'clit', 'clitface', 'clitfuck', 'clitoris', 'clits', 'clover clamps', 'clusterfuck', 'cnut', 'cock', 'cock-sucker', 'cockass', 'cockbite', 'cockburger', 'cockeye', 'cockface', 'cockfucker', 'cockhead', 'cockjockey', 'cockknoker', 'cocklump', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmunch', 'cockmuncher', 'cocknose', 'cocknugget', 'cocks', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cockwaffle', 'cok', 'cokmuncher', 'coksucka', 'coochie', 'coochy', 'coon', 'coons', 'cooter', 'coprolagnia', 'coprophilia', 'cornhole', 'cox', 'cracker', 'crap', 'creampie', 'crotte', 'cum', 'cumbubble', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cummer', 'cumming', 'cums', 'cumshot', 'cumslut', 'cumtart', 'cunilingus', 'cunillingus', 'cunnie', 'cunnilingus', 'cunt', 'cuntass', 'cuntface', 'cunthole', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntrag', 'cunts', 'cuntslut', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'dago', 'damn', 'darkie', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'deggo', 'dendrophilia', 'dick', 'dick-sneeze', 'dickbag', 'dickbeaters', 'dickface', 'dickfuck', 'dickfucker', 'dickhead', 'dickhole', 'dickjuice', 'dickmilkÂ\\xa0', 'dickmonger', 'dicks', 'dickslap', 'dicksucker', 'dicksucking', 'dicktickler', 'dickwad', 'dickweasel', 'dickweed', 'dickwod', 'dike', 'dildo', 'dildos', 'dingleberries', 'dingleberry', 'dink', 'dinks', 'dipshit', 'dirsa', 'dirty pillows', 'dirty sanchez', 'dlck', 'dog style', 'dog-fucker', 'doggie style', 'doggiestyle', 'doggin', 'dogging', 'doggy style', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'donkeyribber', 'doochbag', 'dookie', 'doosh', 'double dong', 'double penetration', 'doublelift', 'douche', 'douche-fag', 'douchebag', 'douchewaffle', 'dp action', 'dry hump', 'duche', 'dumass', 'dumb ass', 'dumbass', 'dumbcunt', 'dumbfuck', 'dumbshit', 'dumshit', 'dvda', 'dyke', 'eat my ass', 'ecchi', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'erotic', 'erotism', 'escort', 'eunuch', 'f u c k', 'f u c k e r', 'f_u_c_k', 'f4nny', 'fag', 'fagbag', 'fagfucker', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggotcock', 'faggs', 'fagot', 'fagots', 'fags', 'fagtard', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'felch', 'felching', 'fellate', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingerbang', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fingering', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'fisting', 'flamer', 'flange', 'foah', 'fook', 'fooker', 'foot fetish', 'footjob', 'frotting', 'fuck', 'fuck buttons', 'fuck off', 'fucka', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbutt', 'fuckbutter', 'fucked', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckheads', 'fuckhole', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktards', 'fucktart', 'fucktwat', 'fuckup', 'fuckwad', 'fuckwhit', 'fuckwit', 'fuckwitt', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'futanari', 'fux', 'fux0r', 'g-spot', 'gang bang', 'gangbang', 'gangbanged', 'gangbangs', 'gay', 'gay sex', 'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'god damn', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'goddamnit', 'gokkun', 'golden shower', 'goo girl', 'gooch', 'goodpoop', 'gook', 'goregasm', 'gringo', 'grope', 'group sex', 'guido', 'guro', 'hand job', 'handjob', 'hard core', 'hard on', 'hardcore', 'hardcoresex', 'heeb', 'hell', 'hentai', 'heshe', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'homo', 'homodumbshit', 'homoerotic', 'honkey', 'hooker', 'hore', 'horniest', 'horny', 'hot carl', 'hot chick', 'hotsex', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack Off', 'jack-off', 'jackass', 'jackoff', 'jaggi', 'jagoff', 'jail bait', 'jailbait', 'jap', 'jelly donut', 'jerk off', 'jerk-off', 'jerkass', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jism', 'jiz', 'jizm', 'jizz', 'juggs', 'jungle bunny', 'junglebunny', 'kawk', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knob', 'knobbing', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kooch', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'kunja', 'kunt', 'kyke', 'l3i+ch', 'l3itch', 'labia', 'lameass', 'lardass', 'leather restraint', 'leather straight jacket', 'lemon party', 'lesbian', 'lesbo', 'lezzie', 'lmfao', 'lolita', 'lovemaking', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'make me come', 'male squirting', 'masochist', 'master-bate', 'masterb8', 'masterbat', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mcfagget', 'menage a trois', 'mick', 'milf', 'minge', 'missionary position', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'mound of venus', 'mr hands', 'muff', 'muff diver', 'muffdiver', 'muffdiving', 'munging', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nambla', 'nawashi', 'nazi', 'negro', 'neonazi', 'nig nog', 'nigaboo', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niglet', 'nimphomania', 'nipple', 'nipples', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'nsfw images', 'nude', 'nudity', 'numbnuts', 'nut sack', 'nutsack', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'orgy', 'p0rn', 'paedophile', 'paki', 'panooch', 'panties', 'panty', 'pawn', 'pecker', 'peckerhead', 'pedobear', 'pedophile', 'pegging', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'phone sex', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'piece of shit', 'pigfucker', 'pimpis', 'piss', 'piss pig', 'pissed', 'pissed off', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'pisspig', 'playboy', 'pleasure chest', 'pole smoker', 'polesmoker', 'pollock', 'ponyplay', 'poof', 'poon', 'poonani', 'poonany', 'poontang', 'poop', 'poop chute', 'poopchute', 'poopuncher', 'porch monkey', 'porchmonkey', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'prince albert piercing', 'pron', 'pthc', 'pube', 'pubes', 'punanny', 'punany', 'punta', 'pusse', 'pussi', 'pussies', 'pussy', 'pussylicking', 'pussys', 'pust', 'puto', 'queaf', 'queef', 'queer', 'queerbait', 'queerhole', 'quim', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', 'renob', 'retard', 'reverse cowgirl', 'rimjaw', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'ruski', 'rusty trombone', 's.o.b.', 's&m', 'sadism', 'sadist', 'sand nigger', 'sandler', 'sandnigger', 'sanger', 'santorum', 'scat', 'schlong', 'scissoring', 'screwing', 'scroat', 'scrote', 'scrotum', 'seks', 'semen', 'sex', 'sexo', 'sexy', 'shag', 'shagger', 'shaggin', 'shagging', 'shaved beaver', 'shaved pussy', 'shemale', 'shi+', 'shibari', 'shit', 'shitass', 'shitbag', 'shitbagger', 'shitblimp', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 'shitdick', 'shite', 'shited', 'shitey', 'shitface', 'shitfaced', 'shitfuck', 'shitfull', 'shithead', 'shithole', 'shithouse', 'shiting', 'shitings', 'shits', 'shitspitter', 'shitstain', 'shitted', 'shitter', 'shitters', 'shittiest', 'shitting', 'shittings', 'shitty', 'shiz', 'shiznit', 'shota', 'shrimping', 'skank', 'skeet', 'skullfuck', 'slag', 'slanteye', 'slut', 'slutbag', 'sluts', 'smeg', 'smegma', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'son-of-a-bitch', 'spac', 'spic', 'spick', 'splooge', 'splooge moose', 'spooge', 'spook', 'spread legs', 'spunk', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'suckass', 'sucks', 'suicide girls', 'sultry women', 'swastika', 'swinger', 't1tt1e5', 't1tties', 'tainted love', 'tard', 'taste my', 'tea bagging', 'teets', 'teez', 'testical', 'testicle', 'threesome', 'throating', 'thundercunt', 'tied up', 'tight white', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'titty', 'tittyfuck', 'tittywank', 'titwank', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'turd', 'tushy', 'tw4t', 'twat', 'twathead', 'twatlips', 'twats', 'twatty', 'twatwaffle', 'twink', 'twinkie', 'two girls one cup', 'twunt', 'twunter', 'unclefucker', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'v14gra', 'v1gra', 'va-j-j', 'vag', 'vagina', 'vajayjay', 'venus mound', 'viagra', 'vibrator', 'violet wand', 'vjayjay', 'vorarephilia', 'voyeur', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wankjob', 'wanky', 'wet dream', 'wetback', 'white power', 'whoar', 'whore', 'whorebag', 'whoreface', 'willies', 'willy', 'wop', 'wrapping men', 'wrinkled starfish', 'xrated', 'xx', 'xxx', 'yaoi', 'yellow showers', 'yiffy', 'zoophilia', 'zubb', 'a$$', 'a$$hole', 'a55hole', 'ahole', 'anal impaler', 'anal leakage', 'analprobe', 'ass fuck', 'ass hole', 'assbang', 'assbanged', 'assbangs', 'assfaces', 'assh0le', 'beatch', 'bimbo', 'bitch tit', 'bitched', 'bloody hell', 'bootee', 'bootie', 'bull shit', 'bullshits', 'bullshitted', 'bullturds', 'bum boy', 'butt fuck', 'buttfuck', 'buttmunch', 'c-0-c-k', 'c-o-c-k', 'c-u-n-t', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'caca', 'cacafuego', 'chi-chi man', 'child-fucker', 'clit licker', 'cock sucker', 'corksucker', 'corp whore', 'crackwhore', 'dammit', 'damned', 'damnit', 'darn', 'dick head', 'dick hole', 'dick shy', 'dick-ish', 'dickdipper', 'dickflipper', 'dickheads', 'dickish', 'f-u-c-k', 'f.u.c.k', 'fist fuck', 'fuck hole', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuck-ass', 'fuck-bitch', 'fuck-tard', 'fuckedup', 'fuckmeat', 'fucknugget', 'fucktoy', 'fuq', 'gassy ass', 'h0m0', 'h0mo', 'ham flap', 'he-she', 'hircismus', 'holy shit', 'hom0', 'hoor', 'jackasses', 'jackhole', 'middle finger', 'moo foo', 'naked', 'p.u.s.s.y.', 'piss off', 'piss-off', 'rubbish', 's-o-b', 's0b', 'shit ass', 'shit fucker', 'shiteater', 'son of a bitch', 'son of a whore', 'two fingers', 'wh0re', 'wh0reface']
    for item in invalid_list:
        if item == string_to_analize:
            return True
    return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_code(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)

def verify_user(user: str, verified_input: int):
    try:
        found_user = users.query.filter_by(username=user).first()
        found_user.verified = verified_input
        db.session.commit()
        print("USER: " + user + " -> VERIFIED: " + verified_input)
    except:
        print("Could not complete this task.")

def match_security(session_type: str, match_id: str) -> bool: #this is for all of the control routes
    found_match = match.query.filter_by(_id=match_id).first()
    try:
        if 'coach' in session[session_type] and found_match.created_by == session[session_type][0]:
            return True
        else:
            return False
    except:
        return False

@app.route("/FAQ")
def FAQ():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("FAQ.html", data=found_user)

@app.route("/about")
def about():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("about.html", data=found_user)

@app.route("/termsofservice")
def termsofservice():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("termsofservice.html", data=found_user)

@app.route("/privacypolicy")
def privacypolicy():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("privacypolicy.html", data=found_user)

@app.route("/chooseprofilepicture")
def chooseprofilepicture():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("chooseprofilepic.html", data=found_user)
    else:
        return render_template("login.html")


@app.route("/newprofilepicture")
def newprofilepicture():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("profile-pic-animation.html", data=found_user)
    else:
        return render_template("login.html")

@app.route("/dashboard/edit_profile")
def edit_profile():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("edit_profile.html", data=found_user)
    else:
        return render_template("login.html")

@app.route("/entering_match/<match_code>")
def entering_match(match_code):
    found_match = match.query.filter_by(match_code=match_code).first()
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("player-or-spectator.html", data=found_user, match_data=found_match)


@app.route("/joincode", methods=['POST', 'GET'])
def joincode():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    if request.method == 'POST':
        code_entry = request.form['code_entry']
        found_match = match.query.filter_by(match_code=code_entry).first()
        if found_match:
            if found_match.match_password == "":
                print('No password!')
                #route to live player dashboard
            return redirect(url_for('entering_match', match_code=found_match.match_code))
        return render_template("join_code_page.html", data="We can't find that match... Please check your join code and try again.")
    return render_template("join_code_page.html", data=None)

@app.route("/box_office/<match1>", methods=['GET', 'POST'])
def box_office(match1):
    match1 = match.query.filter_by(_id=match1).first()
    eventtype = (match1.event_type, match1.teams1.split("~"))
    if request.method == 'POST':
        password = request.form['password_entry']
        name = request.form['name_entry']
        if password == match1.match_password and not sanitize_inputs(name):
            if match1.event_type == 'Singles':
                tuple_data = (request.form['name_entry'], None)
            elif match1.event_type == 'Teams':
                tuple_data = (request.form['name_entry'], request.form['team_select'])
            try:
                Scoring.add_to_lobby(match1._id, tuple_data)
                session['active_player'] = name
            except:
                return redirect(url_for('error', msg="Sorry. This match is not yet live or there was a problem creating a live match file. Please check with your match administrator for more information."))
            return redirect(url_for('player_match_view', json_data_input=match1._id))
        else:
            return redirect(url_for("error", msg='Sorry. Your password was incorrect or your name was inapropriate. Please try again!'))
    return render_template('box_office.html', data=match1, data1=eventtype)

@app.route("/")
def index():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("index.html", data=found_user)

@app.route("/header", methods=['GET'])
def header():
    if 'active_user' in session:
        return render_template("header.html")
    return render_template("error.html", message="Sorry, you do not have access to this page.")

@app.route("/error/<msg>")
def error(msg):
    return render_template("error.html", message=msg)

@app.route("/login", methods=["POST", "GET"])
def login():
    found_user = ""
    if 'active_user' in session:
        return redirect(url_for('dashboard'))
    if request.method == "POST":

        username_input = request.form['username']
        password_input = request.form['password']
        found_user = users.query.filter_by(username=username_input).first()
        

        if found_user and found_user.username == username_input and found_user.password == hashingalg.hashPassword(password_input):
            session['active_user'] = [found_user.username, found_user.name, found_user.rank]
            found_user.last_login = datetime.now()
            db.session.commit()
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", data=found_user, message="Username and password were incorrect! Please try again.")

    return render_template("login.html", data=found_user)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    logged_in_user = found_user
    date_year = str(found_user.first_login)
    date_year = date_year[0:4]

    date = datetime.strptime(str(found_user.first_login), "%Y-%m-%d %H:%M:%S.%f")
    month_index = date.month

    list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_name = list_of_months[month_index-1]

    #chooses three random users
    count = users.query.count()
    random_offset = randint(0, count - 1)
    random_offset2 = randint(0, count - 1)
    random_offset3 = randint(0, count - 1)
    random_user_one = users.query.offset(random_offset).limit(1).first()
    random_user_two = users.query.offset(random_offset2).limit(1).first()
    random_user_three = users.query.offset(random_offset3).limit(1).first()
    while (random_user_one._id == logged_in_user._id):
        random_offset = randint(0, count - 1)
        random_user_one = users.query.offset(random_offset).limit(1).first() 
    while (random_user_two._id == random_user_one._id or random_user_two._id == logged_in_user._id):
        random_offset2 = randint(0, count - 1)
        random_user_two = users.query.offset(random_offset2).limit(1).first() 
    while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id or random_user_three._id == logged_in_user._id):
        random_offset3 = randint(0, count - 1)
        random_user_three = users.query.offset(random_offset3).limit(1).first() 
    random_users_list = [random_user_one, random_user_two, random_user_three]

    #find recent matches
    recent_matches = match_archive.query.filter_by(username=session['active_user'][0]).all()
    recent_matches = [(get_archived_match(thing.filename), thing.date_added) for thing in recent_matches]
    recent_matches = recent_matches[::-1]
    print(recent_matches)

    if 'active_user' in session:
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                    return redirect(url_for('error', msg="Sorry, you have input an inapropriate or non-existant value. Please try again."))

            found_user.team = request.form['team']
            found_user.name = request.form['name']
            found_user.bio = request.form['bio']
            


            db.session.commit()

        return render_template("dashboard.html", month = month_name, random_users_list=random_users_list, recent_matches=recent_matches, year=date_year, data=found_user)
    return redirect(url_for('error', msg="You must login to access this page."))

@app.route("/profile/<user>", methods=['GET', 'POST'])
def get_user_profile(user):
    try:
        found_user = users.query.filter_by(username=user).first()
        date_year = str(found_user.first_login)
        date_year = date_year[0:4]

        date = datetime.strptime(str(found_user.first_login), "%Y-%m-%d %H:%M:%S.%f")
        month_index = date.month

        list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_name = list_of_months[month_index-1]
    except:
        return redirect(url_for('error', msg="Sorry, that user does not exist."))
    
    #find recent matches
    recent_matches = match_archive.query.filter_by(username=user).all()
    recent_matches = [(get_archived_match(thing.filename), thing.date_added) for thing in recent_matches]
    recent_matches = recent_matches[::-1]
    
    try:
        logged_in_user = users.query.filter_by(username=session['active_user'][0]).first()
        print(logged_in_user.name)
        if logged_in_user.username == user:
            return redirect(url_for('dashboard'))
        else:
            #chooses three random users
            count = users.query.count()
            random_offset = randint(0, count - 1)
            random_offset2 = randint(0, count - 1)
            random_offset3 = randint(0, count - 1)
            random_user_one = users.query.offset(random_offset).limit(1).first()
            random_user_two = users.query.offset(random_offset2).limit(1).first()
            random_user_three = users.query.offset(random_offset3).limit(1).first()
            while (random_user_one._id == logged_in_user._id):
                random_offset = randint(0, count - 1)
                random_user_one = users.query.offset(random_offset).limit(1).first() 
            while (random_user_two._id == random_user_one._id or random_user_two._id == logged_in_user._id):
                random_offset2 = randint(0, count - 1)
                random_user_two = users.query.offset(random_offset2).limit(1).first() 
            while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id or random_user_three._id == logged_in_user._id):
                random_offset3 = randint(0, count - 1)
                random_user_three = users.query.offset(random_offset3).limit(1).first() 
            random_users_list = [random_user_one, random_user_two, random_user_three]
    except:
        logged_in_user = None
        count = users.query.count()
        random_offset = randint(0, count - 1)
        random_offset2 = randint(0, count - 1)
        random_offset3 = randint(0, count - 1)
        random_user_one = users.query.offset(random_offset).limit(1).first()
        random_user_two = users.query.offset(random_offset2).limit(1).first()
        random_user_three = users.query.offset(random_offset3).limit(1).first()
        while (random_user_two._id == random_user_one._id):
            random_offset2 = randint(0, count - 1)
            random_user_two = users.query.offset(random_offset2).limit(1).first() 
        while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id):
            random_offset3 = randint(0, count - 1)
            random_user_three = users.query.offset(random_offset3).limit(1).first() 
        random_users_list = [random_user_one, random_user_two, random_user_three]

    return render_template("user_profile_page.html", month = month_name, recent_matches=recent_matches, year=date_year, random_users_list=random_users_list, data1=found_user, data=logged_in_user)
    
@app.route("/create_match", methods=['GET', 'POST'])
def create_match():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
    if 'active_user' in session and session['active_user'][2] == "coach":
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                        break
                        return render_template('create_match.html', message="You have inputed an invalid value or an inapropriate value.")
            
            ezfix = request.form["hometeam"] + '~' + request.form["awayteam"]
            

            try:
                new_match = match(request.form['matchname'], request.form['coursename'], request.form['starttime'], request.form['endtime'], ezfix, request.form['matchname'], generate_code(6), request.form['matchpassword'], request.form['eventtype'], request.form['matchtype'], request.form['numberofplayers'], session['active_user'][0], False)
                db.session.add(new_match)
                db.session.commit()
            except Exception as err:
                print(err)
                return redirect(url_for('error', msg="There was an error in creating your match."))

            return redirect(url_for('match_dashboard'))
        
        return render_template('create_match.html', course_data=found_course, data=found_user)
    return redirect(url_for('error', msg='You do not have access to this page.'))

@app.route("/edit_match/<match_to_edit>", methods=["POST", "GET"])
def edit_match(match_to_edit):
    found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
    found_match = match.query.filter_by(_id=match_to_edit).first()
    if found_match.match_live == 1:
        return redirect(url_for('error', msg="You cannot edit match details of matches that are live!"))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                    if request.form["eventtype"] != "singles" and request.form["hometeam"] == "" and request.form["awayteam"] == "":
                        break
                    return render_template('edit_match.html', data=found_user, message="You have inputed an invalid value or an inapropriate value.", editing=found_match)
            
            ezfix = request.form["hometeam"] + '~' + request.form["awayteam"]

            try:
                found_match.event_type = request.form['eventtype']
                found_match.match_type = request.form['matchtype']
                found_match.teams1 = ezfix
                found_match.total_players = request.form['numberofplayers']
                found_match.match_name = request.form['matchname']
                found_match.match_course = request.form['coursename']

                print(request.form['coursename'])
                found_match.start_time = request.form['starttime']
                found_match.end_time = request.form['endtime']
                found_match.match_password = request.form['matchpassword']
                db.session.commit()
                print(found_match.teams1)
            except:
                redirect(url_for('error', msg="There was a problem adding your match to the database. Please make sure you have inputed all fields. If all else fails, contact customer suport."))
            
            return redirect(url_for("match_dashboard"))

        return render_template('edit_match.html', course_data=found_course, data=found_user, editing=found_match)

    return render_template("error", msg="You do not have access to this site!")


@app.route("/edit_course/<course_to_edit>", methods=["POST", "GET"])
def edit_course(course_to_edit):
    found_course = course.query.filter_by(_id=course_to_edit).first()
    if 'active_user' in session and session['active_user'][0] == found_course.created_by and session['active_user'][2] == "coach":
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method == "POST":
            found_course.course_name = request.form['course-name']
            found_course.course_holes = request.form['numberholes']
            found_course.par1 = request.form['holepar1']
            found_course.par2 = request.form['holepar2']
            found_course.par3 = request.form['holepar3']
            found_course.par4 = request.form['holepar4']
            found_course.par5 = request.form['holepar5']
            found_course.par6 = request.form['holepar6']
            found_course.par7 = request.form['holepar7']
            found_course.par8 = request.form['holepar8']
            found_course.par9 = request.form['holepar9']
            found_course.par10 = request.form['holepar10']
            found_course.par11 = request.form['holepar11']
            found_course.par12 = request.form['holepar12']
            found_course.par13 = request.form['holepar13']
            found_course.par14 = request.form['holepar14']
            found_course.par15 = request.form['holepar15']
            found_course.par16 = request.form['holepar16']
            found_course.par17 = request.form['holepar17']
            found_course.par18 = request.form['holepar18']
            found_course.city = request.form['city']
            found_course.bio = ""
        
            db.session.commit()

            return redirect(url_for("course_dashboard"))
    
    return render_template('edit_course.html', data=found_user, editing=found_course)


@app.route("/delete_match/<match_to_delete>")
def delete_match(match_to_delete):
    found_match = match.query.filter_by(_id=match_to_delete).first()
    if found_match.match_live == 1:
        return redirect(url_for('error', msg="You cannot delete matches that are live!"))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        #removes json file
        try:
            filename = str(found_match._id) + ".json"
            os.remove(os.path.join(app.config['SCORING_FOLDER'], str(filename)))
            #removes match from DB
            db.session.delete(found_match)
            db.session.commit()
            return redirect(url_for("match_dashboard"))
        except:
            db.session.delete(found_match)
            db.session.commit()
            return redirect(url_for("match_dashboard"))
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/delete_course/<course_to_delete>")
def delete_course(course_to_delete):
    found_course = course.query.filter_by(_id=course_to_delete).first()
    if 'active_user' in session and session['active_user'][0] == found_course.created_by and session['active_user'][2] == "coach":
        db.session.delete(found_course)
        db.session.commit()
        return redirect(url_for("course_dashboard"))
    return redirect(url_for('error', msg="You do not have access to this page."))

@app.route("/create_account", methods=['POST', 'GET'])
def create_account():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    if request.method == "POST":
        for item in request.form:
            if request.form[item] == "" or sanitize_inputs(request.form[item]):
                return redirect(url_for('error', msg="Your value was either blank or inapropriate. Please input all correct values. The problem is with the field: [add go back code]" + request.form[item]))
        found_username = users.query.filter_by(username=request.form['username']).first()
        found_email = users.query.filter_by(email=request.form['email']).first()
        if found_username or found_email:
            return render_template('create_account.html', message="Sorry, the email or username you entered is already in use.", data=found_user)
        try: 
            today_date = datetime.now()
            password = hashingalg.hashPassword(request.form['password'])
            print(password)
            new_user = users(request.form['name'], request.form['username'], password, request.form['email'], request.form['rank'], request.form['gender'], request.form['bio'], request.form['team'], 0, "defaultprofilepicture.png", "BigBluebanner.png", today_date, today_date)
            db.session.add(new_user)
            db.session.commit()
            new_username = request.form['username']
            new_rank = request.form['rank']
            new_name = request.form['name']
        except:
            return redirect(url_for('error', msg="There was a problem adding your account to the database. Please make sure you have inputed all fields. If all else fails. Contact customer support."))
        found_user = users.query.filter_by(username=new_username).first()
        
        session['active_user'] = [new_username, new_name, new_rank]
        return redirect(url_for('chooseprofilepicture'))
    return render_template('create_account.html', data=found_user)

@app.route("/delete_account")
def delete_account():

    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    db.session.delete(found_user)
    db.session.commit()

    session.pop('active_user')

    return redirect(url_for('index'))

@app.route("/edit_user_profile", methods=["POST"])
def edit_user_profile():
    if request.method == "POST" and 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        found_user.team = request.form['team']
        found_user.name = request.form['name']
        found_user.bio = request.form['bio']
        found_user.email = request.form['email']

        db.session.commit()

        return redirect(url_for("dashboard"))
    return redirect(url_for('error', msg="Something went wrong. Please try again!"))


@app.route("/choose_banner", methods=["POST"])
def choose_banner():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    if request.method == "POST" and 'active_user' in session:
        found_user.banner = request.form['banner']
        db.session.commit()

        return redirect(url_for("dashboard"))
    return redirect(url_for('error', msg="Something went wrong. Please try again!"))


@app.route("/upload_profile_pic", methods=["POST"])
def upload_profile_pic():
    if request.method == "POST" and 'active_user' in session:
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(url_for('error', msg="Sorry, you did not upload an image file. Please try again!"))
        file = request.files['file']
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' or sanitize_inputs(file.filename):
            return redirect(url_for("error", msg="Sorry, your file did not have a name. Please try again."))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return redirect(url_for("error", msg="Sorry, there was a problem uploading your file. You might need to contact customer support!"))

        if filename == found_user.pic:
                    return redirect(url_for('newprofilepicture'))

        if found_user.pic != 'defaultprofilepicture.png':
            try:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], found_user.pic))
            except:
                found_user.pic = filename        
        found_user.pic = filename
        db.session.commit()

        return redirect(url_for('newprofilepicture'))
    
    return redirect(url_for('error', msg="You do not have access to this site"))

@app.route("/logout")
def logout():
    if 'active_user' in session: 
        session.pop('active_user')
        return redirect(url_for('index'))
    return redirect(url_for('error', msg="How can you log out... if you are not logged in?"))

@app.route("/admin/<password>")
def admin(password):
    if password == "aW1wdmVyc3VzZHdhcmY":
        return render_template("admin.html")
    else:
        return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/match_dashboard")
def match_dashboard():
    if 'active_user' in session and session['active_user'][2] == 'coach':
        found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
        found_match = match.query.filter_by(created_by=session['active_user'][0]).all()
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("match_dashboard.html", course_data=found_course, data=found_user, match_data=found_match)
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/course_dashboard")
def course_dashboard():
    if 'active_user' in session and session['active_user'][2] == 'coach':
        found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("course_dashboard.html", data=found_user, course_data=found_course)
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route('/start_match/<match_id>/<course_id>')
def start_match(match_id, course_id):
    found_match = match.query.filter_by(_id=match_id).first()
    found_course = course.query.filter_by(_id=course_id).first()
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    print(session['active_user'][0], found_match.created_by)
    if found_match.match_live == 1:
        return redirect(url_for('error', data=found_user, msg='This match has already started. Try refreshing your match dashboard to gain access.'))
    elif found_match.match_live == 2:
         return redirect(url_for('error', data=found_user, msg='This match has finished. Try creating another match.'))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][0] == found_course.created_by:
        #match_live is updated in database, from 0 (not live) to 1 (live)
        found_match.match_live = 1
        db.session.commit()

        #creates json
        Scoring.create_json(
            found_match._id, 
            found_match.match_code,
            found_match.match_password,
            found_course.course_holes, 
            found_match.match_name, 
            found_match.start_time, 
            found_match.end_time, 
            found_match.teams1.split("~")[0], 
            found_match.teams1.split("~")[1], 
            found_match.event_type, 
            found_match.match_type,
            found_match._id,
            found_course.par1,
            found_course.par2,
            found_course.par3,
            found_course.par4,
            found_course.par5,
            found_course.par6,
            found_course.par7,
            found_course.par8,
            found_course.par9,
            found_course.par10,
            found_course.par11,
            found_course.par12,
            found_course.par13,
            found_course.par14,
            found_course.par15,
            found_course.par16,
            found_course.par17,
            found_course.par18

        )
        return redirect(url_for("active_match_view", json_data_input=found_match._id))
    else:
        return redirect(url_for('error', data=found_user, msg='You do not have access to this site.'))
    
   

@app.route("/return_user_data/<password>", methods=['GET'])
def return_user_data(password):
    print("hi")
    if password == "123":
        return return_admin_data()
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

@app.route("/change_verified_status/<admin>/<user>/<verified>")
def change_verified_status(admin, user, verified):
    if admin == '123':
        verify_user(user, verified)
        return 'USER: ' + user + " verification status has changed!",200
    else:
        return 'Sorry, you do not have access to this site.'

@app.route("/spectator_match_view/<json_data_input>")
def spectator_match_view(json_data_input):
    scores = []
    try:
        found_match = match.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
        print("LOCATION: " + match_location)
        found_match_owner = users.query.filter_by(username=match_owner).first()
    except:
        found_match = match_archive.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
        print("LOCATION: " + match_location)
        found_match_owner = users.query.filter_by(username=match_owner).first()
    try:
        json_data = Scoring.return_data(json_data_input)
        try:
            found_user = users.query.filter_by(username=session['active_user'][0]).first()
            if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
            else:
                scores = Scoring.calc_match_results(json_data['match_info']['id'])
        except:
            found_user = ''
            if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
            else:
                scores = Scoring.calc_match_results(json_data['match_info']['id'])
        return render_template("spectator-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data = scores)
    except:
        try:
            json_data = Scoring.return_archive_data(json_data_input)
            try:
                found_user = users.query.filter_by(username=session['active_user'][0]).first()
                if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                else:
                    scores = Scoring.calc_match_results(json_data['match_info']['id'])
            except:
                found_user = ''
                if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                else:
                    scores = Scoring.calc_match_results(json_data['match_info']['id'])
            return render_template("spectator-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data = scores)
        except:
            return redirect(url_for('error', msg='This match does not exist!'))


@app.route("/player_match_view/<json_data_input>", methods=['GET', 'POST'])
def player_match_view(json_data_input):
    if 'active_player' in session:
        json_data = None
        try:
            found_match = match.query.filter_by(_id=json_data_input).first()
            match_owner = found_match.created_by
            match_date = found_match.start_time
            match_course = found_match.match_course
            found_course = course.query.filter_by(created_by=match_owner).first()
            match_location = found_course.city
            print("LOCATION: " + match_location)
            found_match_owner = users.query.filter_by(username=match_owner).first()
        except:
            found_match = match_archive.query.filter_by(_id=json_data_input).first()
            match_owner = found_match.created_by
            match_date = found_match.start_time
            match_course = found_match.match_course
            found_course = course.query.filter_by(created_by=match_owner).first()
            match_location = found_course.city
            print("LOCATION: " + match_location)
            found_match_owner = users.query.filter_by(username=match_owner).first()
        try:
            json_data = Scoring.return_data(json_data_input)
        except:
            return redirect(url_for('error', msg='This match is not yet live.'))

        
        if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
            try:
                scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                json_data = Scoring.return_data(json_data_input)
                print(scores)
            except:
                json_data = Scoring.return_data(json_data_input)
        else:
            scores = Scoring.calc_match_results(json_data['match_info']['id'])
        
        

        try:
            found_user = users.query.filter_by(username=session['active_user'][0]).first()
        except:
            found_user = ''
        if request.method =="POST":
            return redirect(url_for("player_match_view", date=match_date, course=match_course, city=match_location, data1=found_match_owner, active_player=session['active_player'], json_data_input = json_data['match_info']['id']))
        return render_template("player-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, active_player=session['active_player'], data=found_user, playerdata=json_data, scoring_data = scores)
    else:
        return redirect(url_for('error', msg='You do not have access to this site until you join a match.'))
    
@app.route("/active_match_view/<json_data_input>")
def active_match_view(json_data_input):
    json_data = None
    try:
        found_match = match.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
        print("LOCATION: " + match_location)
        found_match_owner = users.query.filter_by(username=match_owner).first()
    except:
        found_match = match_archive.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
        print("LOCATION: " + match_location)
        found_match_owner = users.query.filter_by(username=match_owner).first()
    try:
        json_data = Scoring.return_data(json_data_input)
    except:
        return redirect(url_for('error', msg='This match is not yet live.'))
    scores = []
    found_user=''
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ''

    if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
        scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
        players_used = []
        for player in json_data["players"]:
            try:
                opponent = json_data["players"][player]["opponent"]
                players_used.append(player)
                players_used.append(opponent)
            except:
                continue
        

    elif json_data['match_info']['gamemode'] == 'Stroke Play' and json_data['match_info']['match_type'] == 'Teams':
        scores = Scoring.calc_match_results(json_data['match_info']['id'])

    if match_security('active_user', json_data_input):
        return render_template("active_match_view.html", date=match_date,  course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data=scores, rank=session['active_user'][2])
    else:
        return redirect(url_for('error', userdata=found_user, msg="You do not have access to this site!"))

@app.route("/create_course", methods=['GET', 'POST'])
def create_course():
    if 'active_user' in session and session['active_user'][2] == 'coach':
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method =="POST":

            for item in request.form:
                if sanitize_inputs(item) or 'numberholes' not in request.form:
                    return render_template("create_course.html", message='Your values were either blank or inapropriate. Please try again.')


            course_entry = course(request.form["course-name"], request.form["numberholes"], request.form["holepar1"], request.form["holepar2"], request.form["holepar3"], request.form["holepar4"], request.form["holepar5"], request.form["holepar6"], request.form["holepar7"], request.form["holepar8"], request.form["holepar9"], request.form["holepar10"], request.form["holepar11"], request.form["holepar12"], request.form["holepar13"], request.form["holepar14"], request.form["holepar15"], request.form["holepar16"], request.form["holepar17"], request.form["holepar18"], request.form['city'], '', session['active_user'][0])
            db.session.add(course_entry)
            db.session.commit()
            found_course = course.query.filter_by(created_by=session['active_user'][0]).all()

            return redirect(url_for("course_dashboard"))

        return render_template("create_course.html", data=found_user)
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

@app.route("/change_message/<filename>/<message>")
def change_message(filename, message):
    if match_security('active_user', filename):
        Scoring.change_message(filename, message)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/kick_player/<filename>/<player>", methods=['GET', 'POST'])
def kick_player(filename, player):
    if match_security('active_user', filename):
        player = player.replace("%20", " ")
        Scoring.kick_player(filename, player)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/add_player/<filename>/<team>/<player_name>", methods=['GET', 'POST'])
def add_player(filename, team, player_name):
    if match_security('active_user', filename):
        Scoring.add_player(filename, team, player_name)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/edit_score/<filename>/<player>/<hole>/<new_score>")
def edit_score(filename, player, hole, new_score):
    if match_security('active_user', filename) or session['active_player']: #check if this is player
        try:
            new_score = re.sub('[^\d]', '', new_score)
            Scoring.edit_score(filename, player, hole, new_score)
        except:
            return redirect(url_for('error', msg='Please input a vaild value. Integers are required.'))
        if "active_user" in session:
            return redirect(url_for("active_match_view", json_data_input=filename))
        elif "active_player" in session:
            return redirect(url_for("player_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/end_match/<filename>")
def end_match(filename):
    #TODO: ARCHIVE DATA
    if match_security('active_user', filename):
        try:
            del session['active_player']
        except:
            pass

        found_match = match.query.filter_by(_id=filename).first()
        found_match.match_live = 2

        current_time = datetime.now()
        new_entry = match_archive(session['active_user'][0], filename, current_time)
        db.session.add(new_entry)

        db.session.commit()

        archive_match(filename)
        os.remove('static/score_files/' + filename + '.json')

        return redirect(url_for("index"))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/change_opponent/<filename>/<player1>/<player2>")
def change_opponent(filename, player1, player2):
    if match_security('active_user', filename):
        Scoring.change_opponent(filename, player1, player2)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/calc_relation/<filename>/<player>", methods=["GET"])
def calc_relation(filename, player):
    preview = Scoring.calc_relation_to_par(filename, player)
    print(preview)
    return preview, 200

@app.route("/calc_match/<filename>/<player1>/<player2>", methods=["GET"])
def calc_match(filename, player1, player2):
    #try:
    preview = Scoring.calc_match_status(filename, player1, player2)
    print(preview)
    #except:
        #return redirect(url_for('error', msg="Please enter a integer."))
    return preview, 200

@app.route("/lowest_team_score/<filename>", methods=["GET"])
def lowest_team_score(filename):
    try:
        preview = Scoring.get_lowest_team_score(Scoring.get_team_scores(filename))
    except:
        return redirect(url_for('error', msg="There was an error in calculating the lowest team score."))

    if len(preview[0]) > 1:
        return_string = ', '.join(preview[0])
        return return_string, 200
    else:
        return preview[0][0]

@app.route("/search/<searchbar>", methods=["GET", "POST"])
def search(searchbar):
    found_user = ""
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    keyword = searchbar
    if (searchbar == ""):
        keyword = "404"
    search_query = db.session.query(users).filter(
        db.or_(
            users.username.like(f"%{keyword}%"),
            users.name.like(f"%{keyword}%")
        )).limit(100)
    return render_template("search_results.html", keyword=keyword, search_query=search_query, data=found_user)
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, port=8000, debug=True)