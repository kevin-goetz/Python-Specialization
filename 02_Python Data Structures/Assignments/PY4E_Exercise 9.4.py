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
