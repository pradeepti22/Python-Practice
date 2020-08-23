fh=open("mbox-short.txt")
counts=dict()
hour=list()
for line in fh:
    if line.startswith('From '):
        words=line.split()
        hour.append(words[5].split(':')[0])
for h in hour:
    counts[h]=counts.get(h,0)+1
for key,value in sorted(counts.items()):
    print(key,value)
