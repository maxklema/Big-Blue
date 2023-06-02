"""
#Purpose: calculates the single round differential for a player based on the parameters
#Parameters:
  - score - total (gross) round score
  - slope_rating - slope rating from the tees that the player was playing from
  - course_rating - course rating from the tees that the player was playing from
"""
def calc_differential(score, slope_rating, course_rating):
    return float(int((113 / slope_rating) * (score - course_rating)* 10)/10)

"""
#Purpose: calculate a players handicap index 
"""
def calc_index(scores, slope_ratings, course_ratings):
    best_eight = []
    sum = 0
    num = 0
    if (len(scores) > 8 and len(scores) < 20):
        for s in range(len(scores)):
            if len(best_eight) < 8:
                best_eight.append(calc_differential(scores[s], slope_ratings[s], course_ratings[s]))
            else:
                worst = -20
                for i in range(len(best_eight)):
                    if worst < best_eight[i]:
                        worst = best_eight[i]
                if scores[s] < worst:
                    best_eight.remove(worst)
                    best_eight.append(scores[s])
    elif len(scores) >= 20:
        for s in range(len(scores) - 20, len(scores)):
            if len(best_eight) < 8:
                best_eight.append(calc_differential(scores[s], slope_ratings[s], course_ratings[s]))
            else:
                worst = -20
                for i in range(len(best_eight)):
                    if worst < best_eight[i]:
                        worst = best_eight[i]
                if scores[s] < worst:
                    best_eight.remove(worst)
                    best_eight.append(scores[s])
    else:
        for s in range(len(scores)):
            best_eight.append(scores[s])
    
    for k in range(len(best_eight)):
        sum += calc_differential(scores[k], slope_ratings[k], course_ratings[k])
        num += 1
    return float(int((sum / num) * 10)/10)

""" 
Purpose: calculate a players handicap for a given course 
"""
def calc_course_handicap(index, slope_rating, course_rating, par):
    #Course Handicap = Handicap Index® x (Slope Rating™ / 113) + (Course Rating™ – par)
    return index * (slope_rating / 113) + (course_rating - par)

"""
#Purpose: adjust handicap based on the allowed amount of handicap provided
"""
def adjust_handicap(course_handicap, percent):
    return course_handicap * (percent / 100)

"""
#Purpose: calculates the amount of strokes that a player recieves on each hole during a round
"""
def calc_strokes(course_handicap, handicaps):
    strokes = []
    while course_handicap > 0:
        for i in range(len(handicaps)):
            dif = 0
            if handicaps[i] <= chand:
                dif = 1
            else:
                dif = 0
            if len(strokes) == 18:
                strokes[i] += dif
            else:
                strokes.append(dif)
        course_handicap -= 18
    return strokes