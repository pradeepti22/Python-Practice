def totalTicketCost(A,B,C):
    classA = 200.85; classB = 450.75;  classC = 675.95
    classATax = 5.6; classBTax = 10.3; classCTax = 5.6
    
    costA = classA * A
    taxCostA = costA * (classATax / 100)
    totalCostA = costA + taxCostA
    
    costB = classB * B
    taxCostB = costB * (classBTax / 100)
    totalCostB = costB + taxCostB
    
    costC = classC * C
    taxCostC = costC * (classCTax / 100)
    totalCostC = costC + taxCostC
    
    totalSeatCost = totalCostA + totalCostB + totalCostC
    if C > 0:
        finalSeatCost = totalSeatCost - (totalSeatCost * 0.04)
        discount = 'DISCOUNT APPLIED'
        discountedAmount = totalSeatCost * 0.04
    else:
        finalSeatCost = totalSeatCost
        discount = 'NO DISCOUNT'
        discountedAmount = 0

    print('Class A Seats\tSeat Tax Rate\tClass A Cost\t Class A Tax Cost\tTotal Class A Seat Cost')
    print(str(A) + ' @ $' + str(classA) + '\t' + format(classATax,'.1f') + '%\t\t$' + format(costA,',.2f') + '   \t$' + format(taxCostA,'.2f') + '\t\t\t$' + format(totalCostA,',.2f'))
    print()
    print('Class B Seats\tSeat Tax Rate\tClass B Cost\t Class B Tax Cost\tTotal Class B Seat Cost')
    print(str(B) + ' @ $' + str(classB) + '\t' + format(classBTax,'.1f') + '%\t\t$' + format(costB,',.2f') + '   \t$' + format(taxCostB,'.2f') + '\t\t\t$' + format(totalCostB,',.2f'))
    print()        
    print('Class C Seats\tSeat Tax Rate\tClass C Cost\t Class C Tax Cost\tTotal Class C Seat Cost')
    print(str(C) + ' @ $' + str(classC) + '\t' + format(classCTax,'.1f') + '%\t\t$' + format(costC,',.2f') + '   \t$' + format(taxCostC,'.2f') + '\t\t\t$' + format(totalCostC,',.2f'))
    print()
    print(discount + '...\t$' + format(discountedAmount,',.2f'))
    print('TOTAL COST OF PURCHASE IS: $' + format(finalSeatCost,',.2f'))
    print('______________________________________________________________________________________')
    
    
totalTicketCost(5,9,2)
print()
totalTicketCost(11,1,0)

def paintJobCost(S):
    if S < 2001:
        paint = 9.53
    else:
        paint = 10.50

    labor = 35
    hazard = 0.075

    paintRequired = (S / 112)
    paintCost = paintRequired * paint
    laborRequired = (S / 112) * 8
    laborCost = laborRequired * labor
    hazardFee = hazard * paintCost
    TotalCost = paintCost + laborCost + hazardFee
    
    print('________________________________________LOCKLEAR PAINT COMPANY__________________________________________')
    print('Square Footage\tPaint Required\tPaint Cost\tLabor Hours\t Labor Cost\tHazard Fee\tTOTAL COST OF PAINT JOB')
    print(str(S) + '\t\t' + format(paintRequired,'.2f') + ' gal\t$' + format(paintCost,',.2f') + '\t\t' + format(laborRequired,'.2f') + ' hrs\t $'
          + format(laborCost,',.2f') + '\t$' + format(hazardFee,',.2f') + '\t\t$' + format(TotalCost,',.2f'))
    

print()
paintJobCost(1800)
print()
paintJobCost(2700)
print()
paintJobCost(3200)
