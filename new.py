import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.meshkovbrest.by/files/editor_Заявление_на_частичный_возврат_Вардар20221.doc')
.encode

for line in fhand :
    print (line.decode().strip())

