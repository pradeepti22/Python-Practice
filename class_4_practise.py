#Prob 1

print('YEAR\tOLD TUITION COST\tPERCENT INCREASE\tNEW TUITION COST\tTUITION INCREASE')
tuition=8000
percent=3
new_tuition=0
tuition_increase=0

for i in range(1,6):
    new_tuition=(tuition*percent/100)+tuition
    tuition_increase=new_tuition-tuition
    print(i,'\t','$',format(tuition,',.2f'),'\t\t',format(percent/100, '.0%'),'\t\t\t','$',format(new_tuition,',.2f'),'\t\t','$',format(tuition_increase,',.2f',))
    percent=percent+3
    tuition=new_tuition

print('_______________CREATED BY PRADEEPTI UPADHYAYULA')



#Prob 2

print('MONTH\tMONTHLY SALES\tSTATE TAX AMOUNT\tFED TAX AMOUNT\tTOTAL TAX AMOUNT\tSALES TAX')

sale=1000
month=1
st_tax=0
fd_tax=0
tot=0

while month<=6:
    st_tax=(sale*0.05)
    fd_tax=(sale*0.025)
    tot=st_tax+fd_tax
    stax=sale-tot
    
    print(month,'\t','$',format(sale,',.2f'),'\t','$',format(st_tax, ',.2f'),'\t\t','$',format(fd_tax,',.2f'),'\t','$',format(tot,',.2f'),'\t\t','$',format(stax, ',.2f'))
    
    if month==5:
        sale=(sale*0.07)+sale     
    else:
        sale=(sale*0.10)+sale
    
    month=month+1
                                                                                                                                            
print('_______________CREATED BY PRADEEPTI UPADHYAYULA')


