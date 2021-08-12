# %%

'''
Exercise 12.7:
Write a program that reads the HTML from the data files below,
and parse the data, extracting numbers
and compute the sum of the numbers in the file.
'''

# import relevant libraries
import re  # noqa
import requests  # noqa
from bs4 import BeautifulSoup as bs  # noqa

# read the html
url = 'http://py4e-data.dr-chuck.net/comments_1159498.html'
html = requests.get(url).text

# parse the html
soup = bs(html, 'html.parser')
tag = soup('span')

# find all numbers and compute the sum
numbers = re.findall('[0-9]+', str(tag))
print(numbers)
print(sum(int(n) for n in numbers))
