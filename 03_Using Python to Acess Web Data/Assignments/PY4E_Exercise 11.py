# %%

'''
Exercise 11:
The basic outline of this problem is to read the file,
look for integers using the re.findall(),
looking for a regular expression of '[0-9]+'
and then converting the extracted strings to
integers and summing up the integers.
'''
# omport thr regular expression library
import re  # noqa

# open and read the whole txt-file
filename = 'regex_sum_1159496.txt'
data = open(filename).read()

# find 1 or more numbers and add to the list
listed = re.findall('[0-9]+', data)
numbers = len(listed)

# print the results and sum up the numbers
print('The Data contains {} numbers.'.format(numbers))
print(sum(int(i) for i in listed))

# %%

'''
Extra Exercise:
Write a Python program to check that a string
contains only a certain set of characters
(in this case a-z, A-Z and 0-9).
'''

# import the regular expression library
import re  # noqa


# define the regex function
def char_correct(string):
    pattern = '[^a-zA-Z0-9]'
    if re.search(pattern, string):
        return 'Incorrect character!'
    else:
        return 'all fine'


# test the regex function
string1 = 'sjfheiusflgh893247243u89'
char_correct(string1)

# %%

'''
Extra Exercise:
Write a program that gives back
the sum of the numbers in this string:
"Hello 129 isdjfk 2.4569 hi -12.2 +hello ++12 --1.2".
'''

# import the regular expression library
import re  # noqa

# define test string and regex
text = "Hello 129 isdjfk 2.4569 hi -12.2 +hello ++12 --1.2"
listed = re.findall(r'-?\d+\.?\d+', text)

# print the results
print('This is the list:', listed)
listed_sum = sum(float(i) for i in listed)
print('This is the sum of the list:', round(listed_sum, 2))
