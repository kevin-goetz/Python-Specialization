# %%
# Worked example Chapter 12.4
# 1. Reading it as a text-file into a string (like the .read())

import requests  # noqa
romeo = requests.get('http://data.pr4e.org/romeo.txt')
print(romeo.text)

# %%

# Worked example Chapter 12.4
# 2. Count and print lines

# import the library, get the html
import requests  # noqa
romeo = requests.get('http://data.pr4e.org/romeo.txt')
linecode = 1

# loop through the lines of the file and print the line number
for line in romeo.iter_lines(decode_unicode=True):
    print('Line {}:'.format(linecode), line)
    linecode += 1

# close the file
romeo.close()

# %%

# Worked example Chapter 12.4
# 3. Count the words from the html site

# import the library, get the html and split it into its words
import requests  # noqa
romeo = requests.get('http://data.pr4e.org/romeo.txt')
words = romeo.text.split()
word_dict = dict()

# loop through the list with the words from the txt-file
for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

# print the unsorted dict
print('unsorted:')
print(word_dict)

# print the sorted dict
print('\nsorted:')
print(dict(sorted(word_dict.items(),
      reverse=True, key=lambda item: item[1])))

# close the file
romeo.close()
