from setup import *

class New_Courses(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    created_by = db.Column(db.String)
    address = db.Column(db.String(75))
    holes = db.Column(db.String(3))
    tees = db.Column(db.String)
    pars = db.Column(db.String)
    hole_handicaps = db.Column(db.String)
    course_ratings = db.Column(db.String)
    slope_ratings = db.Column(db.String)
    distances = db.Column(db.String)

    def __init__(self, name, created_by, address, num_holes, tees, pars_from_tees, handicaps_from_tees, course_ratings_from_tee, slope_ratings_from_tees, distances_from_tees):
        self.name = name
        self.created_by = created_by
        self.address = address
        self.holes = num_holes
        self.tees = tees
        self.pars = pars_from_tees
        self.hole_handicaps = handicaps_from_tees
        self.course_ratings = course_ratings_from_tee
        self.slope_ratings = slope_ratings_from_tees
        self.distances = distances_from_tees

    def get_course_info(self, tee_name):
        index = -1
        for i in self.tees:
            if i == tee_name:
                index = self.tees.index(i)
        
        if index == -1:
            print("There is no tee by the name \"" + tee_name + "\"")
            return 
        
        if self.distances == []:
            return {"tees": tee_name, "pars": self.pars[index], "handicaps": self.hole_handicaps[index], "slope_rating": self.slope_ratings[index], "course_rating": self.course_ratings[index]}
        
#c = Course("Example Course", "11 Main Street", 18, ["red", "green"], [[4,4,5,4,3,4,3,4,5,4,4,5,4,3,4,3,4,5], [4,4,5,4,3,4,3,4,5,4,4,5,4,3,4,3,5,5]], [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,17]], [70, 75], [112, 120], 1)

#print(c.get_course_info("green"))