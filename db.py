import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():
        database = sqlite3.connect('.database/liftlog.db')
        database.row_factory = sqlite3.Row
        return database

def GetAllSessions():
    database = GetDB()
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
    result = database.execute(
         'SELECT * FROM Sessions WHERE id=?', (session_id,)
    ).fetchone()
    database.close()
    return result