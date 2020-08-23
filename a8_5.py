fname=input("Enter file name: ")
fh=open(fname)
count=0
lst=list()
for line in fh:
    if line.startswith('From '):
        words=line.split()
        email=words[1]
        lst.append(email)
        count=count+1
for i in lst:
    print(i)
print("There were", count, "lines in the file with From as the first word")
