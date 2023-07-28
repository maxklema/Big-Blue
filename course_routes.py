from setup import *

def list_to_string(list_one: list):
    return str(list_one)

'''
def delete():
    New_Courses.query.delete()
    db.session.commit()

def transfer_matches():
    courses = course.query.all()
    new_courses_list = []

    for thing in courses:
        c = New_Courses(thing.course_name, thing.created_by, thing.city, thing.course_holes, "['main']","[["+str(thing.par1)+","+str(thing.par2)+","+str(thing.par3)+","+str(thing.par4)+","+str(thing.par5)+","+str(thing.par6)+","+str(thing.par7)+","+str(thing.par8)+","+str(thing.par9)+","+str(thing.par10)+","+str(thing.par11)+","+str(thing.par12)+","+str(thing.par13)+","+str(thing.par14)+","+str(thing.par15)+","+str(thing.par16)+","+str(thing.par17)+","+str(thing.par18)+"]]",None, None, None, None)
        new_courses_list.append(c)
    
    for item in new_courses_list:
        db.session.add(item)
    
    db.session.commit()

def add_column():
    with app.app_context():
        alter_query = text('ALTER TABLE new__courses ADD COLUMN created_by VARCHAR(255);')
        db.session.execute(alter_query)
        db.session.commit()


@app.route("/test")
def test():
    delete()
    transfer_matches()
    return 'Working',200
'''

@app.route("/create_course_new", methods=['GET', 'POST'])
def create_course_new():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method =="POST":

            if session['active_user'][2] == 'coach':

                return redirect(url_for("course_dashboard"))

            elif session['active_user'][2] == 'player':

                return redirect(url_for("course_dashboard"))

        return render_template("create_course_new.html", data=found_user)
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

@app.route('/create_new_course_submit', methods=['POST', 'GET'])
def create_new_course_submit():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method == 'POST':
            
            number_of_holes = request.form['numberholes']
            course_name = request.form['course-name']
            address = request.form['course-location']

            tee_names_list = []
            tee_slope_list = []
            tee_course_list = []
            tee_par_list = []
            tee_yardage_list = []
            tee_handicap_list = []

            for i in range(1,9):
                try:
                    tee_names_list.append(request.form['Tee-'+str(i)+'-name-input'])
                    tee_slope_list.append(request.form['tee-'+str(i)+'-slope-rating'])
                    tee_course_list.append(request.form['tee-'+str(i)+'-course-rating'])
                    par_list = []
                    yardage_list = []
                    handicap_list = []
                
                    for j in range(1,int(number_of_holes)+1):
                        par_list.append(request.form["hole_" + str(j) + "_par_at_tee_" + str(i)])
                        yardage_list.append(request.form["hole_" + str(j) + "_yardage_at_tee_" + str(i)])
                        handicap_list.append(request.form["hole_" + str(j) + "_handicap_at_tee_" + str(i)])
                    
                    tee_par_list.append(par_list)
                    tee_yardage_list.append(yardage_list)
                    tee_handicap_list.append(handicap_list)

                except:
                    break
                    
            c = New_Courses(course_name, session['active_user'][0], address, number_of_holes, list_to_string(tee_names_list), list_to_string(tee_par_list), list_to_string(tee_handicap_list), list_to_string(tee_course_list), list_to_string(tee_slope_list), list_to_string(tee_yardage_list), 0)
            db.session.add(c)
            db.session.commit()

            return redirect(url_for("course_dashboard"))
        else:
            return rediret(url_for("error", msg="Sorry, something went wrong. Please try again."))
    else:
        return rediret(url_for("error", msg="Sorry, you do not have permission to access this page."))

@app.route("/db_update", methods=['POST'])
def db_update():

    with app.app_context():
        alter_query = text(request.form['command'])
        db.session.execute(alter_query)
        db.session.commit()
    
    return "DONE",200


@app.route("/course_profile/<course_id>")
def course_profile(course_id):
    found_user = ""
    found_course = New_Courses.query.filter_by(_id=course_id).first()
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("course_profile.html", data=found_user, course_data=found_course)

@app.route("/add_favorite_course/<course_id>", methods=['POST','GET'])
def add_favorite_course(course_id):
    if 'active_user' in session:
        active_user_db = users.query.filter_by(username=session['active_user'][0]).first()
        favored_courses = string_to_list(active_user_db.favored_courses)
        if favored_courses != None:
            if int(course_id) not in favored_courses:
                favored_courses.append(int(course_id))
        else:
            favored_courses = [course_id]
        active_user_db.favored_courses = str(favored_courses)
        db.session.commit()
        return redirect(url_for('course_profile', course_id=course_id))
    else:
        return redirect(url_for('error', msg='You must be logged in to add a course to your profile.'))
    
