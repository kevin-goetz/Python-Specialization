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
