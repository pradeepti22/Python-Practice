def computepay(h,r):
    h=float(h)
    r=float(r)
    if h<=40:
        rate=h*r
    elif h>40:
        rate=(h-40)*1.5*r + 40*r
    return rate
hours = input('Enter hours:')
rate = input('Enter pay:')
print(computepay(hours,rate))
