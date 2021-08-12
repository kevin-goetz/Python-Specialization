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
