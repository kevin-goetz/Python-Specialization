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
