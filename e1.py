from itertools import count
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter the link:')
uh = urllib.request.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)
root = tree.getroot()


lst = list()
print (tree.get('.//count'))
# for items in tree.findall('.//count') :
#     lst.append(int(items.text))
# #lst.append(tree.findall('.//count'))
# print (sum(lst))


