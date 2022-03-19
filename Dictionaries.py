purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 3
print(purse)
#{'money': 12,'tissues': 75'candy': 3}
print(purse['candy'])
#3

#count items in dict

counts = dict()
names = ['ivan', 'vova', 'vova', 'lesha', 'sasha', 'lesha']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
#P{'ivan': 1, 'lesha': 2,'vova':2, 'sasha':1}

#the get method in dictionaries

if name in counts:
    x = counts[name]
else:
    x = 0

 x = counts.get(name, 0)

#fastest waY:
counts = dict()
names = ['ivan', 'vova', 'vova', 'lesha', 'sasha', 'lesha']
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)

#covert dict to list #values() keys() list. .items()

jjj = {'money': 12,'tissues': 75'candy': 3}
print(list(jjj))
#['money','tissues','candy']
print(jjj.keys())
#['money','tissues','candy']
print(jjj.values())
#[12, 3, 75]
print(jjj.items())
[('candy': 3),('money': 12),('tissues': 75)]

#.item() two iteration variables

jjj = {'money': 12,'tissues': 75'candy': 3}
for aaa,bbb in jjj.items() :
    print(aaa,bbb)
#candy 3
#money 12
#tissues 75

#count every word in the text

name = input ('enter fiile:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bogword = None
for word,count in counts.items():
    if bigcount is None or count > bogcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
