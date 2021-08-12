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
