from logging import NullHandler
from urllib.request import urlopen
#import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter:')
pos = input ('Position:')
pos = int(pos)
count = input ('Count:')
count = int(count)
#lsturl = list()
#lst = list()


for i in range(count+1):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print ("Retrive:", url)
    lst = list()
    lsturl = list()
    for tag in tags :
        y = tag.get('href', None)
        lst.append(y)
    
    url = lst[pos-1]
       
    lsturl.append(url)