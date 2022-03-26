import urllib.request
import json
import xml.etree.ElementTree as ET


inp = input ('enter the link:')


url = urllib.request.urlopen(inp)
newurl = url.read()

info = json.loads(newurl)
#print (json.dumps(info, indent=4))
#print (type(info))

lst = list()
print (info.keys())
for u in info['comments'] :
    item = u['count']
    lst.append(int(item))

print (sum(lst))
# for u in info[1]:
#     print (u['comments'][0]['count'])

    # print (u['comments'][0]['count'])



