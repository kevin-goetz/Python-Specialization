# %%

'''
Exercise 15.3:
This application will read roster data in JSON format, parse the file, and
then produce an SQLite database that contains a User, Course, and Member
table and populate the tables from the data file.
Once you have written the program and it has been run successfully reading
the above JSON data, run the following SQL command:

SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X;

Find the first row in the resulting record set and enter the long string that
looks like 53656C696E613333.
'''

# import and connect
import sqlite3 as sql  # noqa
import json  # noqa


# load the json file
string = open('./roster_data.json').read()
js = json.loads(string)

# connect to the DB
conn = sql.connect('./rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# loop through the json file and extract the infos
for i in js:
    name = i[0]
    cur.execute('''
    insert or ignore into user (name)
    values (?) ''', (name,))
    cur.execute('''
    select id from user where name = ?''', (name,))
    user_id = cur.fetchone()[0]

    title = i[1]
    cur.execute('''
    insert or ignore into course (title)
    values (?) ''', (title,))
    cur.execute('''
    select id from course where title = ?''', (title,))
    course_id = cur.fetchone()[0]

    role = i[2]
    cur.execute('''
    insert or ignore into member (user_id, course_id, role)
    values (?, ?, ?) ''', (user_id, course_id, role))

    # commit is essential!
    conn.commit()

# close the connection to the database
cur.close()
conn.close()
