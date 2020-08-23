fh = open("mbox-short.txt")
content=list()
count=dict()
for line in fh:
    if line.startswith('From '):
        fline=line.split()
        content.append(fline[1])
for word in content:
    count[word]=count.get(word,0)+1
memail=None
mcount=None
for key,value in count.items():
    if mcount is None or value>mcount:
        memail=key
        mcount=value
print(memail, mcount)
