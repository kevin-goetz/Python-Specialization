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
