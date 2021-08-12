# %%

'''
Exercise 10.2:
10.2 Write a program to read through the mbox-short.txt
and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from
the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

# file path, file handle and initial variable
filename = 'mbox-short.txt'
fhandle = open(filename)
fdict = dict()

# loop through lines of the txt-file
# and find the time and its count
for line in fhandle:
    if 'From ' in line:
        flist = line.split(':')
        hourline = flist[0].strip()
        hour = hourline[-2:]
        fdict[hour] = fdict.get(hour, 0) + 1
    else:
        continue

# close the file
fhandle.close()

# sort and print the results
hour_list = sorted(fdict.items())
for k, v in hour_list:
    print(k, v)
