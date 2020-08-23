#Class 3 - Tuples and lists

#Prob 1

A=[1,2,3,4,5]
print(A)

#Prob 2

A=[1,2,3,4,5]
x=sum(A)
print(x)

#OR

A=[1,2,3,4,5]

i=0
sum=0
while i<len(A):
    sum=sum+A[i]
    i=i+1

print(sum)

#Prob 3

A=[1,2,3,4,5]
prod=1
for i in A:
    if i%2==0:
        prod=prod*i
print(prod)


#Prob 4
B=list(range(8,10))
print(B)


#Prob 5
A=[1,2,3,4,5]
B=[8,9]
C=A+B
print(C)


#Prob 6
A=[1,2,3,4,5]
B=[8,9]
C=[1,2,3,4,5,8,9]

#sum of odd numbers
sumo=0
for i in C:
    if i%2==1:
        sumo=sumo+i
print(sumo)

#sum of even numbers
sume=0
for i in C:
    if i%2==0:
        sume=sume+i
print(sume)

print(sumo-sume)


#Prob 7 even numbers greater than 4 in C

C=[1,2,3,4,5,8,9]
D=[]

i=0
while i<len(C):
    if C[i]%2==0 and C[i]>4:
        D.append(C[i])
    i=i+1
print(D)


# Prob 8 - CHECK THIS GODDAMN THING
C=[1,2,3,4,5,8,9]
C.reverse()
print(C)


# Prob 9
C=[1,2,3,4,5,8,9]
print(C[3:7])


# Prob 10

A=[1,2,3,4,5]

for i in A:
    if i%2!=0:
        A.remove(i)
print(A)
    

# Prob 11

A=[1,2,3,4,5]
b=tuple(A)
print(b)
















