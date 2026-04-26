-- Database queries


--CREATE TABLE IF NOT EXISTS Users (
--    id  INTEGER PRIMARY KEY AUTOINCREMENT,
--    username TEXT NOT NULL UNIQUE,
--    password TEXT NOT NULL
--);

--CREATE TABLE IF NOT EXISTS Sessions (
--    id         INTEGER PRIMARY KEY AUTOINCREMENT,
--    user_id    INTEGER NOT NULL,
--    date       TEXT    NOT NULL,
--    exercise   TEXT    NOT NULL,
--    sets       INTEGER NOT NULL,
--    reps       INTEGER NOT NULL,
--    weight_kg  REAL    NOT NULL,
--    FOREIGN KEY (user_id) REFERENCES Users(id)
--)