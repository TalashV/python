
from logging import NullHandler
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = input ('Enter position:')
count = input ('Enter count:')
position = int(position)
count = int(count)


for i in range(count+1) :
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print ('Retriving', url)
    lst = list()
    urllist = list()
    for tag in tags :
        tag1 = tag.get('href', None)
        lst.append(tag1)
    
    url = lst[position-1]

    urllist = urllist.append(url)












# while xcount != count :
#     if html == None :
#         readlink(tag1)
#         for tag in tags:
#             if x != position :
#                 x = x + 1
#                 continue
#             else :
#                 tag1 = tag.get('href', None)
#                 print("Retrieving:", tag1)
#                 xcount = xcount + 1
#                 x = 0
#             break
#     else :
#         for tag in tags:
#             if x != position :
#                 x = x + 1
#                 print(x)
#                 continue
#             else :
#                 tag1 = tag.get('href', None)
#                 print("Retrieving:", tag1)
#                 xcount = xcount + 1
#                 x = 0
#                 html == None
#             break