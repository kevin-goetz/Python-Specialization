# %%

'''
Exercise 8.5:
Open the file mbox-short.txt and read it line by line.
When you find a line that starts with
'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split()
and print out the second word in the line
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
Also look at the last line of the sample output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

mbox = open('mbox-short.txt')       # user prompt
mlist = list()                      # initialize empty list
count = 0                           # initialize variable

for i in mbox:                      # loop through the lines of the txt.-file
    if 'From ' in i:
        hlist = i.split()           # split the line into a list of words
        mlist.append(hlist[1])      # take the second word and append it
        count += 1                  # line count
    else:
        continue

for i in mlist:                     # print out the list's words
    print(i)

# give a summary and close the file
print('There were', count, 'lines in the file with From as the first word')
mbox.close()
