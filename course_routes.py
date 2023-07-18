from setup import *


def list_to_string(list_one: list):
    print(list_one)
    return str(list_one)


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
                    print("LIST CHECK")
                    print(tee_names_list)
                    print(tee_slope_list)
                    print(tee_course_list)
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
                    
            c = New_Courses(course_name, address, number_of_holes, list_to_string(tee_names_list), list_to_string(tee_par_list), list_to_string(tee_handicap_list), list_to_string(tee_course_list), list_to_string(tee_slope_list), list_to_string(tee_yardage_list))
            db.session.add(c)
            db.session.commit()

            return redirect(url_for("course_dashboard"))
        else:
            return rediret(url_for("error", msg="Sorry, something went wrong. Please try again."))
    else:
        return rediret(url_for("error", msg="Sorry, you do not have permission to access this page."))




            

