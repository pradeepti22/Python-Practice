#Practise exam

# task 1

def totalTicketCost(a,b,c):
    acost=200.85
    bcost=450.75
    ccost=675.95
    atax=0.056
    btax=0.103
    ctax=0.056
    disc=0
    
    tcost=((a*acost)+(atax*a*acost))+((b*bcost)+(btax*b*bcost))+((c*ccost)+(ctax*c*ccost))

    if c!=0:
        disc=(0.04*tcost)
        tcost=tcost-disc

    print('Class A Seats\tSeat Tax Rate\tClass A cost\tClass A Tax Cost\tTotal Class A Seat Cost')

    print(a,'@','$',acost,'\t',format(atax*100,'.1f'),'%','\t\t','$',format((a*acost),',.2f'),'\t','$',format((atax*a*acost),',.2f'),'\t\t','$',format((a*acost)+(atax*a*acost),',.2f'),'\n')
    
          
    print('Class B Seats\tSeat Tax Rate\tClass B cost\tClass B Tax Cost\tTotal Class B Seat Cost')

    print(b,'@','$',bcost,'\t',format(btax*100, '.1f'),'%','\t','$',format((b*bcost),',.2f'),'\t','$',format((btax*b*bcost),',.2f'),'\t\t','$',format((b*bcost)+(btax*b*bcost),',.2f'),'\n')
              
          
    print('Class C Seats\tSeat Tax Rate\tClass C cost\tClass C Tax Cost\tTotal Class C Seat Cost')

    print(c,'@','$',ccost,'\t',format(ctax*100, '.1f'),'%','\t\t','$',format((c*ccost),',.2f'),'\t','$',format((ctax*c*ccost),',.2f'),'\t\t','$',format((c*ccost)+(ctax*c*ccost),',.2f'),'\n')
    
    if c==0:
        print('NO DISCOUNT . . . $.0.00')
    else:
        print('Discount Applied $'+ format(disc,',.2f'))
    print('Total cost of Purchase is ' + format(tcost, ',.2f'),'\n\n')

totalTicketCost(5,9,2)
totalTicketCost(11,1,0)



#task 2
sqft=0
def paintJobCost(sqft):
    pgal=0
    lab=0
    haz=0
    totcost=0
    labhours=0
    totpaintcost=0
    
    print('_______________________________________LOCKER PAINT COMPANY_____________________________________________')
    print('Square Footage\tPaint Required\tPaint Cost\tLabor Hours\tLabor Cost\tHazard Fee\tTOTAL COST OF PAINT JOB')
    gal=sqft/112
    if sqft <=2000:
        pcost=gal*9.53
    else:
        pcost=gal*10.50
        
    labhours= sqft/14
    labcost=labhours*35
    haz=pcost*0.075
    totcost=pcost+labcost+haz

    print(sqft,'\t\t',format((gal), ',.2f'),'gal','\t','$',format((pcost), ',.2f'),'\t',format((labhours), ',.2f'),'hrs','\t','$',format((labcost), ',.2f'),'\t',\
          '$',format((haz), ',.2f'),'\t','$',format((totcost), ',.2f'),'\n')
    

paintJobCost(1800)
paintJobCost(2700)
paintJobCost(3200)























































