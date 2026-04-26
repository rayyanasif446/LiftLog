#Data base setup and test script
import sqlite3
from werkzeug.security import generate_password_hash

#connect to database file
conn = sqlite3.connect('.database/liftlog.db')

#create the user table to store authentication details
conn.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT    NOT NULL UNIQUE,
        password TEXT    NOT NULL
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS SESSIONS (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id  INTEGER NOT NULL,
        date     TEXT    NOT NULL,
        exercise TEXT    NOT NULL,
        sets     INTEGER NOT NULL,
        reps     INTEGER NOT NULL,
        weight_kg REAL   NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    )
''')

#seed test users 
users = [
('marcus', 'ironmind'),
('priya', 'deadlift99'),
('zach', "squatking"),
('taylah', 'gainz2026'),
('oliver', 'benchpress'),
]

for username, password in users:
    conn.execute(
        'INSERT OR IGNORE INTO Users(username, password) VALUES(?, ?)',
        (username, generate_password_hash(password))
    )
conn.commit()

#seed test workout sessions 
sessions = [
    (1, '10-04-2026', 'Bench Press',            4, 8, 80.0),
    (1, '12-04-2026', 'Incline Dumbell Press',  3, 10, 30.0),
    (2, '11-04-2026', 'Deadlift',               5, 5, 12.0),
    (2, '15-04-2026', 'Lateral Raise',          4, 8, 90.0),
    (3, '10-04-2026', 'Back Squat',             4, 12, 180.0),
    (4, '14-04-2026', 'Leg Press',              4, 10, 80.0),
    (4, '11-04-2026', 'Hip Thrust',             3, 10, 40.0),
    (5, '15-04-2026', 'Bulgarian Split squat',  4, 6, 60.0),
    (5, '12-04-2026', 'Overhead Press',         3, 15, 12.0),
]
#insert all sessions into the same datbase
conn.executemany(
    'INSERT OR IGNORE INTO Sessions '
    '(user_id, date, exercise, sets, reps, weight_kg) '
    ' VALUES(?, ?, ?, ?, ?, ?)',
    sessions
)

conn.commit()
conn.close()
print('database complete')

