#XML - eXtensible Markup Language
import requests
from itertools import count
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#VERSION ONE - ET.PARSE
link = input('Enter link:')
URL = link

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)

tree = ET.parse('feed.xml')
root = tree.getroot()
# root.tag
# root.attrib
lst = list()

#SUM - DONE
for count in root.iter('count') :
    lst.append(int(count.text))

print (sum(lst))

#VERSION TWO - ET.FROMSTRING
url = input('Enter the link:')
uh = urllib.request.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)

lst = list()
for items in tree.findall('.//count') :
    lst.append(int(items.text))
#lst.append(tree.findall('.//count'))
print (sum(lst))
