fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
rfh = fh.read()
count = 0
aa = rfh.split('\n')
for line in aa :
    #    line.strip()
    if line.startswith('From ') : 
        string = line.split()
        print(string[1])
        count = count + 1
        continue
print("There were", count, "lines in the file with From as the first word")