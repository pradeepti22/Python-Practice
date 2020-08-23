#Class exercise 3
'''
#Level 0 task

def geoCalculator(B,C,D,E):
    R1= (B*C) * 0.5
    R2= (B*C) * 0.5
    R3= D*C
    C1 = (3.14*(0.5*E)**0.5)
    area= R1 + R2+ R3+ C1
    return area

print(geoCalculator(10, 10, 12, 8))


#LEVEL 1 TASK1

def combineMe(L1, L2):
    L3=[]
    i=0
    while i < len(L1):
        L3.append(L1[i] + L2[i])
        i=i+1
    return L3

A=['A', 'B', 'C']
B=['D', 'E', 'F']

print(combineMe(A,B))


#level 1 Task 2


def multiplyEven(L):
    prod=1
    for i in L:
        if i%2==0:
            prod=prod*i
    return prod
            
def sumOdd(L):
    sum=0
    for i in L:
        if i%2==1:
            sum=sum+i
    return sum
            
def productSum(L):
    res = multiplyEven(L) + sumOdd(L)
    return res

l=[1,2,3,4]
print(productSum(l))


#level 1 task 3

def frontBackMix(L1,L2,L3):
    NL=[]
    i=0
    while i < len(L1):
        NL.append(L1[i] + L3[len(L3) - (1 + i)])
        NL.append(L2[len(L2) - (1 + i)])
        i=i+1
    return NL

l1=['A','B','C']
l2=['D','E','F']
l3=['G','H','I']
print(frontBackMix(l1,l2,l3))


#level 2

def calc_average(L):
    sum=0
    for i in L:
        sum=sum+i
    avg=sum/len(L)
    return avg

def determine_grade(s):
    grade='A'
    if s > 89:
        grade='A'
    if s > 79 and s < 90:
        grade='B'
    if s > 69 and s < 80:
        grade='C'
    if s > 59 and s <70:
        grade='D'
    if s < 60:
        grade= 'F'
    return grade

def testScoring(L):
    print('Test Scoring Report')
    for i in L:
        print('Score: ' + str(i) + ' ' + determine_grade(i))
    print('Average Score: ' + str(calc_average(L)) + ' ' + determine_grade(calc_average(L)))

A=[85, 95, 87, 91, 80]
print(testScoring(A))
'''    
#level3

def euclidean(X1, Y1, X2, Y2):
    xdiff=(X1-X2)**2
    ydiff=(Y1-Y2)**2
    D = (xdiff + ydiff)**0.5
    return D

P={'P1': ['P1',8,12], 'P2': ['P2',12,38], 'P3': ['P3',34,65], 'P4': ['P4',17,43], 'P5': ['P5',9,22]}
def chartMyDistance(D):
    print('Euclidean Distance Calculations')
    print()
    print('Point\tX\tY\tDistances')
    print(D['P1'][0] + '\t' + str(D['P1'][1]) + '\t' + str(D['P1'][2]) + '\t' + str(euclidean(D['P1'][1],D['P1'][2],D['P3'][1], D['P3'][2])))
    print(D['P2'][0] + '\t' + D['P2'][1] + '\t' + D['P2'][2] + '\t' + str(euclidean(D['P2'][1],D['P2'][2],D['P4'][1], D['P4'][2])))
    print(D['P3'][0] + '\t' + D['P3'][1] + '\t' + D['P3'][2] + '\t' + str(euclidean(D['P3'][1],D['P3'][2],D['P5'][1], D['P5'][2])))
    print(D['P4'][0] + '\t' + D['P4'][1] + '\t' + D['P4'][2] + '\t' + str(euclidean(D['P4'][1],D['P4'][2],D['P1'][1], D['P1'][2])))
    print(D['P5'][0] + '\t' + D['P5'][1] + '\t' + D['P5'][2] + '\t' + str(euclidean(D['P5'][1],D['P5'][2],D['P1'][1], D['P1'][2])))

    print('________________________________')
    

chartMyDistance(P)

#level4

D1={'A': [11,12,13], 'B': [21,22,23], 'C': [31,32,33]}

def modifyMap(D1):
    








