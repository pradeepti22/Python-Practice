'''
#CONDITIONAL STATEMENTS
#Problem 1
x=101
if x>100:
    y=20
    z=40
    print(x,y,z)
else:
    print('The value of x is not greater than 100')


#Problem 2
a=3
if a<10:
    b=0
    c=1
    print(a,b,c)


#Problem 3 if-else
a=20
if a<10:
    b=0
else:
    b=99
print(a,b)


#Problem 4 nested if
amount_1=11
amount_2=99
if amount_1>10:
    if amount_2<100:
        if amount_1>amount_2:
            print(amount_1)
        else:
            print(amount_2)
else:
    print('No condition is met')



#Problem 5 if-elif-else

value_A=200
value_B=250
if value_A==100 and value_B==200:
    print('Optimal values')
elif value_A==70 and value_B==170:
    print('Sub-Optimal values')
elif value_A!=100 and (value_B!=200 or value_B!=170):
    print('Parameters are Unknown')


#Problem 6
speed=100
if speed>24 and speed<56:
    print('Speed is normal')
else:
    print('Speed is abnormal')


#LOOPS

#Problem 1

for i in range(0,21):
    while i%2==0:
        print(i)
        i=i+1


#Problem 2

i=10
while i>0:
    if i%2==1:
        print(i)
    i=i-1
        


#Problem 3

i=0
while i<=30:
    if i%3==0:
        print(i)
    i=i+1


#or

for i in range(0,31):
    while i%3==0:
        print(i)
        i=i+1


#Problem 4

i=0
while i<=20:
    if i%2==1 and i%3!=0:
        print(i)
    i=i+1
    

#Problem 5

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)


#Problem 6

prod=1
for i in range(1,31):
    if i%2==0 and i!=10:
        prod=prod*i
print(prod)


#Problem 7

for i in range(80,7,-1):
    if i%7==0:
        print(i)

'''

#Problem 8

prod=1
for i in range(1,51):
    if i%2==0:
        prod=prod*i
print('The Product of all even numbers between 1-50 is ' + str(prod))

sum=0
for j in range(51,101):
    if j%2==1:
        sum=sum+j
print('The sum of all odd numbers between 51-100 is ' + str(sum))

result=prod-sum
print('The difference between product and sum is '+ str(result))



    
