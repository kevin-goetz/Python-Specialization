# %%

'''
Exercise 6.1:
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing the reverse string in the end.
'''

word = input('Please enter a word:')    # user prompt
reverse = ''                            # initialize variable

for i in word:                          # loop through the word
    reverse = reverse+word[-1]          # add last letter
    word = word[0:-1]                   # shorten the prompt by last letter

print(reverse)                          # print the results

# %%
# Exercise 6.1 in compact form
word2 = input('Please enter a word:')   # user prompt
print(word2[::-1])                      # slicing the whole string to reverse

# %%

'''
Exercise 6.5:
Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"  # initialize the text
substr = text[text.find(':')+1:]        # find the substring (number)
print(float(substr))                    # print the substring as a float


# %%

'''
Exercise 7.1:
Write a program that prompts for a file name,
then opens that file and reads through the file,
and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''

fname = input('Enter the file name:')           # prompt the user

try:
    fhandle = open(fname + '.txt')              # file handling

except:  # noqa
    print('File cannot be opened:', fname)      # if an error occurs
    quit()

print(fhandle.read().upper())                   # print file in capitals


# %%
# Exercise 7.1 variation I
filepath = 'words.txt'
file = open(filepath)
print(file.read())
file.close()

# %%
# Exercise 7.1 variation II
filepath = 'words.txt'
with open(filepath) as f:
    for line in f:
        print(line.rstrip().upper())

# %%

'''
Exercise 7.2:
Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values
from each of the lines and compute the average of those
values and produce an output as shown below.
Do not use the sum() function or a variable named
sum in your solution.
You can download the sample data at
http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt
as the file name.
'''

fname = input('Enter file name:')                  # user prompt
spam = 0                                           # initialize variable
count = 0                                          # initialize variable

with open(fname, 'r') as fhandle:                  # file handling
    for line in fhandle:                           # loop through lines
        if 'X-DSPAM-Confidence:' in line:
            spam += float(line[21:])               # add the numbers
            count += 1                             # count occurrences

print('Average spam confidence:', spam/count)      # print avg. spam confidence

# %%

'''
 Exercise 8.4:
 Open the file romeo.txt and read it line by line.
 For each line, split the line into a list of words using
 the split() method. The program should build a list of
 words.
 For each word on each line check to see if
 the word is already in the list and if not append
 it to the list. When the program completes,
 sort and print the resulting words in alphabetical order.

You can download the sample data at
http://www.py4e.com/code3/romeo.txt
'''

romeo = open('romeo.txt').read()    # user prompt
rolist = romeo.split()              # text to list
ronew = list()                      # setup new empty list

for i in rolist:                    # loop through initial list's words
    if i in ronew:
        continue
    else:
        ronew.append(i)             # add to new list if not already in there

ronew.sort()                        # sort new list alphabetically
print(ronew)                        # print new list

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

# %%

'''
Exercise 9.4:
Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of mail
messages. The program looks for 'From ' lines and takes
the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps
the sender's mail address to a count of the number of
times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using
a maximum loop to find the most prolific committer.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

# initialize variables
filename = 'mbox-short.txt'
fhandle = open(filename)
fdict = dict()

# loop through the txt-file to find the email adresses
# and add them with their count to the dict
for line in fhandle:
    if 'From ' in line:
        flist = line.split()
        for word in flist:
            if '@' in word:
                fdict[word] = fdict.get(word, 0) + 1
    else:
        continue

# close the file
fhandle.close()

# playing around with alternatives

print('Alternative 1:')
print(max(fdict, key=fdict.get), max(fdict.values()))

print('Alternative 2:')
flist_value = list(fdict.values())
max_value = max(flist_value)
max_index = flist_value.index(max_value)
flist_keys = list(fdict.keys())
max_key = flist_keys[max_index]
print(max_key, max_value)

print('Alternative 3:')
big_value = 0
big_key = ''
for key, value in fdict.items():
    if value > big_value:
        big_value = value
        big_key = key
    else:
        continue
print(big_key, big_value)

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
