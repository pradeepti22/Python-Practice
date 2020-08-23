hrs=input('Enter hours:')
h=float(hrs)
pay=input('Enter pay:')
p=float(pay)
if h<=40:
 rate=p*h
elif h>40:
 rate=(h-40)*1.5*p + 40*p
print(rate)
