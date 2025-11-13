import sqlite3

sql_code = """
CREATE TABLE IF NOT EXISTS Movies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
release_year INTEGER,
genre TEXT,
rating REAL
);
"""

sql_code_2 = """
CREATE TABLE IF NOT EXISTS Actors (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
birth_year INTEGER,
nationality TEXT
);
"""

sql_code2k = """
SELECT * FROM Movies
WHERE publish_year > 2010 AND rating > 8
ORDER BY rating DESC;
"""

sql_code2 = """
SELECT DISTINCT genre FROM Movies
ORDER BY genre ASC;
"""

sql_code10 = """
SELECT * FROM Movies
ORDER BY rating ASC
LIMIT 10 OFFSET 10;
"""
sql_code_3 = """
SELECT * FROM Actors WHERE birth_year < 1980;
ORDER BY birth_year ASC;
"""

pupoke = """
SELECT * FROM Movies WHERE genre = "Sci-Fi";
ORDER BY title ASC;
"""

nam= """
SELECT DISTINCT nationality FROM Actors
ORDER BY nationality DESC;
"""

mama = """
SELECT title FROM Movies
WHERE rating <= 5.0;
ORDER BY rating ASC; 
"""

n_select3 = """
SELECT title, release_year FROM Movies
ORDER BY release_year DESC LIMIT 5;
"""
vse = """
SELECT * FROM Actors ORDER BY birth_year ASC LIMIT 3;
"""

oke = """
SELECT COUNT(id) FROM Movies;
"""

code = """
SELECT AVG(rating) FROM Movies;
"""

okak = """
SELECT * FROM Movies WHERE rating<=6.0 AND rating>=8.0
ORDER BY title;
"""
#1.13 ??????

zdravia = """
SELECT * FROM Movies WHERE release_year<=1990 AND release_year>=1990
ORDER BY release_year;
"""
leni = """
SELECT * FROM Movie ORDER BY rating LIMIT 5
"""
