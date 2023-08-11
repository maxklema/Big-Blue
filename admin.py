from setup import *

@app.route('/BBadmin/login', methods=['POST', 'GET'])
def BBadimn():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('error', msg='You do not have access to this site! Leave!'))
    return render_template('admin_login.html')

@app.route("/admin")
def admin():
    if 'admin' in session:
        return render_template("admin.html")
    else:
        return redirect(url_for('error', msg='GET OUT!'))

@app.route("/admin/logout2")
def logout2():
    del session['admin']
    return redirect(url_for('index'))

@app.route("/admin/send_email_notification/<password>", methods=['POST'])
def send_email_notification(password):
    if password == 'graysonisthebestcomposer':
        conn = sqlite3.connect('instance/webdata.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''SELECT * from USERS''')
        result = cursor.fetchall()
        for user in result:
            print("Email sent to: " + user[4])
            try:
                emails1.send_email(user[4], 'Update from BigBlue.golf', request.form['content'])
            except:
                print("Could not sent email to " + user[4])
            print('___' + request.form['content'])
        return render_template("admin.html", message="Messages sent sucsessfuly!")
    else:
        return render_template("admin.html", message="Password was incorrect!")

def return_admin_data():
    db = sqlite3.connect('instance/webdata.sqlite3')
    data = db.execute("select * from users")
    data_dict = {}

    data_dict[0] = {"name": "Name", "username": "Username", "password": "Password", "email": "Email", "rank": "Rank", "gender": "Gender", "bio": "Bio", "team": "Team", "verified": "Verified", "pic": "Picture File"}
    
    for row in data:
        data_dict[len(data_dict)+1] = {"name": row[1], "username": row[2], "password": row[3], "email": row[4], "rank": row[5], "gender": row[6], "bio": row[7], "team": row[8], "verified": row[9], "pic": row[10]}

    return data_dict

@app.route("/return_user_data/<password>", methods=['GET'])
def return_user_data(password):
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