fname=input("Enter file name: ")
fh=open(fname)
tot=0
num=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        value=line[21:26]
        value=float(value)
        tot=tot+value
        num=num+1
avg=tot/num
print("Average spam confidence:", avg)
