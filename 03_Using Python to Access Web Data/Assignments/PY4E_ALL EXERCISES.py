# %%

'''
Exercise 11:
The basic outline of this problem is to read the file,
look for integers using the re.findall(),
looking for a regular expression of '[0-9]+'
and then converting the extracted strings to
integers and summing up the integers.
'''
# import the regular expression library
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

# %%

'''
Worked Example Chapter 12.1:
Get the txt-file via a HTTP request.
'''

import socket  # noqa
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

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

# %%

'''
Exercise  12.5:
Change the socket program so that it only shows the data after the headers
and a blank line have been received.
'''

# import the relevant libraries
import socket  # noqa

# connection and get-request
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

# receiving end decoding the socket answer
data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # end of header
print(message[header_end_pos:], end='')

# receive the first 512 characters and print them
while True:
    data = my_sock.recv(512)
    if not data:
        break
    print(data.decode())

# close the connection
my_sock.close()

# %%
# Testing

import requests  # noqa
from bs4 import BeautifulSoup as bs  # noqa
url = 'http://www.dr-chuck.com/'
html = requests.get(url).text
soup = bs(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

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


# %%

'''
Exercise 13.1:
The program will prompt for a URL, read the XML data
from that URL and then parse and extract
the comment counts from the XML data, compute the sum
of the numbers in the file and print the sum.
'''

# import relevant libraries
import xml.etree.ElementTree as ET  # noqa
import requests  # noqa

# get the xml and parse it
xml = requests.get('http://py4e-data.dr-chuck.net/comments_1159500.xml').content  # noqa
tree = ET.fromstring(xml)
lst = tree.findall('.//comment')  # .// means search through whole tree
lst_num = []

# loop through the comments and find the numbers to cumpote the sum
for comment in lst:
    num = comment.find('count').text
    lst_num.append(int(num))

print(sum(lst_num))

# %%
'''
Exercise 13.2:
The program will prompt for a URL, read the json data
from that URL and then parse and extract
the comment counts from the json data, compute the sum
of the numbers in the file and print the sum.
'''

# import relevant libraries
import requests  # noqa
import json  # noqa

# get the json and parse the json
url = 'http://py4e-data.dr-chuck.net/comments_1159501.json'
resp = requests.get(url).text
json_dict = json.loads(resp)
# print(json.dumps(json_dict, indent=4))

# loop through the json and sum up the numbers
json_counts = []
counts = 0
for data in json_dict['comments']:
    count = data['count']
    counts += int(count)

print(counts)

# %%

'''
Exercise 13.3:
Write a program that uses a GeoLocation lookup API
modelled after the Google API to look up
the University of Kansas and parse the returned data.
'''
# import relevant libraries
import urllib.request, urllib.parse, urllib.error  # noqa
import json  # noqa
import ssl  # noqa

# set key and serviceurl
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# initialize adress and search-url
address = 'University of Kansas'
parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

# request the url's html and decode it
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# loop through the json and print the last place id of the results
try:
    js = json.loads(data)
except:  # noqa
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

# print(json.dumps(js, indent=4))

print(js['results'][-1]['place_id'])

# %%
