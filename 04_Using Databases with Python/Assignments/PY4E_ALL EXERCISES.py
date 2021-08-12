

# %%

'''
Exercise 15.1:
This application will read the mailbox data (mbox.txt)
count up the number email messages per organization
(i.e. domain name of the email address) using a database
with the following schema to maintain the counts:
CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting
database file above for grading. If you run the program multiple
times in testing or with different files, make sure to empty out
the data before each run. The data file for this application is the
same as in previous assignments:
'http://www.py4e.com/code3/mbox.txt'.

Because the sample code is using an UPDATE statement and committing
the results to the database as each record is read in the loop, it might
take as long as a few minutes to process all the data. The commit insists
on completely writing all the data to disk every time it is called.
The program can be speeded up greatly by moving the commit operation outside of
the loop. In any database program, there is a balance between the number of
operations you execute between commits and the importance of not losing the
results of operations that have not yet been committed.
'''

# 1. Imports
import requests
import sqlite3 as sql

# 2. Preparing Connections
# a) Database
conn = sql.connect('./orgdb.sqlite')
cur = conn.cursor()
# b) HTML
resp = requests.get('http://www.py4e.com/code3/mbox.txt', stream=True)

# 3. Preparing DB Table
cur.execute('drop table if exists counts')
cur.execute('create table counts (org text, count integer)')

count = dict()  # test before uploading to database (see EOF)

# 4. Looping through the HTML and adding to DB
for line in resp.iter_lines(decode_unicode=True):
    if line.startswith('From'):
        words = line.split()
        domain = words[1].split("@")
        org = str(domain[1])
        count[org] = count.get(org, 0) + 0.5  # test before uploading to database # noqa
        cur.execute('select count from counts where org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('insert into counts (org, count) values (?, 0.5)', (org,))  # noqa
        else:
            cur.execute('update counts set count = count + 0.5 where org = ?', (org,))  # noqa
conn.commit()


# 5. Testing: Sorting of the Dictionary
count_sort = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))  # noqa
times = 1
for k, v in count_sort.items():
    if times <= 10:
        print(k, int(v))
        times += 1
    else:
        print('\n')
        break


# 6. Final Result in DB
for row in cur.execute('select * from counts order by count desc limit 10'):
    print(row[0], row[1])

# 7. Closing the connections
resp.close()
cur.close()
conn.close()


# %%

'''
Exercise 15.2:
This application will read an iTunes export file in XML and produce a properly
normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

If you run the program multiple times in testing or with different files, make
sure to empty out the data before each run. You can export your own tracks
from iTunes and create a database, but for the database that you turn in for
this assignment, only use the Library.xml data that is provided.
To grade this assignment, the program will run a query like this on your
uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
;
'''

# Imports
import xml.etree.ElementTree as ET  # noqa
import sqlite3  # noqa

# Conect to the DB
conn = sqlite3.connect('./trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# determine the filename of the soundtracks
fname = 'Library.xml'


# define functon to find keys in the xml
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


# parse the xml
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# loop through the records and extract infos
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print(name, artist, genre, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        (name, album_id, genre_id, length, rating, count))  # noqa

    # commit is essential!
    conn.commit()

# close the connection to the DB
cur.close()
conn.close()


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
