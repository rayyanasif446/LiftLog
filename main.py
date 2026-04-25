from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "liftlog_secret"


#HOME
@app.route("/")
def Home():
    sessionData = db.GetAllSessions()
    return render_template('index.html', sessions=sessionData)

app.run(debug=True, port=5000)