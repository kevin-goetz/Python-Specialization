# %%

'''
Exercise 12.6:
Write a program that reads the HTML from the data files below,
extract the href=values from the anchor tags,
scan for a tag that is in the 17th position
from the top and follow that link.
Repeat the process seven times,
and report the last name you find.
'''

# Import the relevant libraries
import re  # noqa
import requests  # noqa
from bs4 import BeautifulSoup as bs  # noqa

# get url and search webpage for all other url
url = 'http://py4e-data.dr-chuck.net/known_by_Jessna.html'
for r in range(7):
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    tag = soup('a')
    tags_list = []
    for t in tag:
        tags_list.append(t.get('href', None))
    url = tags_list[17]
    print('Retrieving: {}'.format(url))
