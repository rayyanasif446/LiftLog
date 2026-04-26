from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "liftlog_secret"


#HOME page
@app.route("/")
def Home():
    sessionData = db.GetAllSessions()
    return render_template('index.html', sessions=sessionData)

#LOGIN page
@app.route('/login', methods=['GET', 'POST'])
def Login():
    #reroutes u to home page if your already logged in
    if session.get('username'):
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.CheckLogin(username, password)
        if user:
            #save user id and username to session
            session['id']       = user['id']
            session['username'] = username
            return redirect('/')
    return render_template('login.html')

#register page
@app.route('/register', methods=['GET', 'POST'])
def Register():

    if session.get('username'):
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.RegisterUser(username, password):
            return redirect('/login')
    return render_template('register.html')


#add page
@app.route('/add', methods=['GET', 'POST'])
def Add():
    # Authorisation, must be logged in
    if session.get('username') is None:
        return redirect('/')
    if request.method == 'POST':
        user_id   = session['id']
        date      = request.form['date']
        exercise  = request.form['exercise']
        sets      = request.form['sets']
        reps      = request.form['reps']
        weight_kg = request.form['weight_kg']
        db.AddSession(user_id, date, exercise, sets, reps, weight_kg)
        return redirect('/')
    return render_template('add.html')

# Edit session
@app.route('/edit/<int:sess_id>', methods=['GET', 'POST'])
def Edit(sess_id):
    if session.get('username') is None:
        return redirect('/')
    record = db.GetSessionById(sess_id)
    if record['user_id'] != session['id']:
        return redirect('/')
    if request.method == 'POST':
        date      = request.form['date']
        exercise  = request.form['exercise']
        sets      = request.form['sets']
        reps      = request.form['reps']
        weight_kg = request.form['weight_kg']
        db.UpdateSession(sess_id, date, exercise, sets, reps, weight_kg)
        return redirect('/')
    return render_template('edit.html', record=record)






app.run(debug=True, port=5000)