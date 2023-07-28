import json

#Scoring class
class Scoring():
    def create_json(filename, match_code, match_password, number_holes, match_name, start_time, end_time, home_team, away_team, match_type, gamemode, Id, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, par17, par18):
        data = {"players":{}, "match_info": {"par1": par1, "par2": par2, "par3": par3, "par4": par4, "par5": par5, "par6": par6, "par7": par7, "par8": par8, "par9": par9, "par10": par10, "par11": par11, "par12": par12, "par13": par13, "par14": par14, "par15": par15, "par16": par16, "par17": par17, "par18": par18, "match_code": match_code, "match_password": match_password, "number_holes": number_holes, "match_name": match_name, "start_time": start_time, "end_time": end_time, "home_team":home_team, "away_team": away_team, "match_type": match_type, "gamemode": gamemode, "id": Id},"lobby":[], "message": "", "shared_coaches": []}
        #json_string = json
        with open("static/score_files/" + str(filename) + ".json", "a+") as file:
            
            #print(json.dump(data, file, indent=3))
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def new_create_json(filename, match_code, match_password, number_holes, match_name, start_time, end_time, num_teams, teams, match_type, gamemode, Id, par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15, par16, par17, par18, shotgun_start):
        data = {"players":{}, "match_info": {"par1": par1, "par2": par2, "par3": par3, "par4": par4, "par5": par5, "par6": par6, "par7": par7, "par8": par8, "par9": par9, "par10": par10, "par11": par11, "par12": par12, "par13": par13, "par14": par14, "par15": par15, "par16": par16, "par17": par17, "par18": par18, "match_code": match_code, "match_password": match_password, "number_holes": number_holes, "match_name": match_name, "start_time": start_time, "end_time": end_time, "team_scores": {}, "match_type": match_type, "gamemode": gamemode, "id": Id},"lobby":[], "message": "", "shared_coaches": []}
        for team in teams:
            data["teams"][team] = 0
        with open("static/score_files/" + str(filename) + ".json", "a+") as file:
            
            #print(json.dump(data, file, indent=3))
            file.seek(0)
            json_object = json.dump(data, file, indent=3)
            file.truncate()

    def add_shared_coach(filename, coach_username):
            with open("static/score_files/" + str(filename) + ".json", "r+") as file:
                file.seek(0)
                data = json.load(file)
                data["shared_coaches"].append(coach_username)
                file.seek(0)
                json_object = json.dump(data, file, indent=3)
                file.truncate()

    def remove_shared_coach(filename, coach_username):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            if coach_username in data["shared_coaches"]:
                data["shared_coaches"].remove(coach_username)
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
                player = player.replace('%20', ' ')
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

    def add_player(filename, player, team, starting_hole=1):
        #json.load("test.json")
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            holes = {}
            if data["match_info"]["number_holes"] == "9":
                holes = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            elif data["match_info"]["number_holes"] == "18":
                holes = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0}
                
            data["players"][player] = {"team": team, "opponent": "","scores":holes,"golf_clap":0,"starting_hole":starting_hole}

            player = player.replace('%20', ' ')
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
                current_score = 0
                current_par = 0
                holes_complete = 0
                
                for i in range(int(data["match_info"]["number_holes"])+1):
                    if (player_score[str(i)] != 0 and player_score[str(i)] != "0"):
                        holes_complete+=1
                        current_score += int(player_score[str(i)])
                        current_par += data["match_info"]["par" + str(i)]

                absolute_relation = str(abs(current_score - current_par))
                if holes_complete == int(data["match_info"]["number_holes"]):
                    return "F: " + str(current_score)
                elif current_score > current_par:
                    return "+" + absolute_relation + " thru " + str(holes_complete)
                elif current_score < current_par:
                    return "-" + absolute_relation + " thru " + str(holes_complete)
                else:
                    return "E" + " thru " + str(holes_complete)
        except:
            with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
                file.seek(0)
                data = json.load(file)
                player_score = data["players"][player]["scores"]
                current_score = 0
                current_par = 0
                holes_complete = 0
                
                for i in range(int(data["match_info"]["number_holes"])+1):
                    if (player_score[str(i)] != 0 and player_score[str(i)] != "0"):
                        holes_complete+=1
                        current_score += int(player_score[str(i)])
                        current_par += data["match_info"]["par" + str(i)]

                absolute_relation = str(abs(current_score - current_par))
                if holes_complete == int(data["match_info"]["number_holes"]):
                    return "F: " + str(current_score)
                elif current_score > current_par:
                    return "+" + absolute_relation + " thru " + str(holes_complete)
                elif current_score < current_par:
                    return "-" + absolute_relation + " thru " + str(holes_complete)
                else:
                    return "E" + " thru " + str(holes_complete)
    
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
    
    def add_golf_clap(filename, player):
        with open("static/score_files/" + str(filename) + ".json", "r+") as file:
            file.seek(0)
            data = json.load(file)
            if player in data["players"]:
                data["players"][player]['golf_clap'] += 1
                file.seek(0)
                json.dump(data, file, indent=3)
                file.truncate()