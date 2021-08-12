# %%

'''
Exercise 15.1:
This application will read the mailbox data (mbox.txt)
count up the number emailmessages per organization
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
