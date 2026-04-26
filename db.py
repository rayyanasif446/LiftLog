import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():
        #Connects to the database file
        database = sqlite3.connect('.database/liftlog.db')
        database.row_factory = sqlite3.Row
        return database

def GetAllSessions():
    database = GetDB()

    #Execute a JOIN query to combine data from the Sessions and Users tables.
    sessions = database.execute('''
        SELECT  Sessions.id, Sessions.user_id, Sessions.date,
                Sessions.exercise, Sessions.sets, Sessions.reps,
                Sessions.weight_kg, Users.username
        FROM Sessions
        JOIN Users ON Sessions.user_id = Users.id
        ORDER BY Sessions.date DESC
    ''').fetchall()
    database.close()
    return sessions

def GetSessionByID(session_id):
    database = GetDB()
    #Filtered SELECT query to find one specific workout session by its ID number
    result = database.execute(
         'SELECT * FROM Sessions WHERE id=?', (session_id,)
    ).fetchone()
    database.close()
    return result

def CheckLogin(username, password):
    database = GetDB()
    # search the database to find a user with the exact username entered
    #(?,) to block SQL injection attacks.
    user = database.execute(
        'SELECT * FROM Users WHERE username=?', (username,)
    ).fetchone()
    if user is not None:
        if check_password_hash(user['password'], password):
            return user
    return None

def RegisterUser(username, password):
    if not username or not password:
        return False
    database = GetDB()
    hashed = generate_password_hash(password)
    database.execute(
        'INSERT INTO Users(username, password) VALUES(?, ?)',
        (username, hashed)
    )
    database.commit()
    return True