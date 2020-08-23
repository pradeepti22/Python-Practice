
#function that counts even numbers in a list
def counteven(L):
    c=0
    for i in L:
        if i%2==0:
            c=c+1
    return c

l=[1,2,3,4,5,6,7,8]
print(counteven(l))

#function that calculates avg of even numbers in a list


def evenavg(L):
    c=0
    sum=0
    avg=0
    for i in L:
        if i%2==0:
            sum=sum+i
            c=c+1
    avg=float(sum/c)
    return avg

l=[1,2,3,4]

print(evenavg(l))    


#function to convert distance in miles to km

def convert(m):
    km=m*1.609
    return km

print(convert(2))
#euclidean distance - the straight line distance between 2 points
#SQRT(X1-X2)^2 + (Y1-Y2)^2. take parameters as points

def eucdist(P1, P2):
    xdiff=(P1[0]-P2[0])**2
    ydiff=(P1[1]-P2[1])**2
    d = (xdiff + ydiff)**0.5
    return d

p=[1,2]
q=[3,4]
print(eucdist(p,q))


#function that gives distance between points 1 and 2 and dist between 3 and 4
#and return the sum of distance

def eucdist4(P1,P2,P3,P4):
    totdist=eucdist(P1,P2)+eucdist(P3,P4)
    return totdist

#function that accepts a list of numbers of grades and gives a letter equivalent

def lettergrade(L):
    gradelist=[]
    for i in L:       
        if i<100 and i>94:
            gradelist.append("A")
        elif i<95 and i>84:
            gradelist.append("B")
        elif i<85 and i>70:
            gradelist.append("C")
        else:
            gradelist.append("F")
    return(gradelist)

p=[60, 97,86,74]
print(lettergrade(p))


#function to take a list of nos., count, gives avg, max, min, sum of numbers

def minvalue(L):
    minv=L[0]
    for i in L:
        if i<minv:
            minv=i
    return minv

def maxvalue(L):
    maxv=L[0]
    for i in L:
        if i>maxv:
            maxv=i
    return maxv

def sumvalue(L):
    lsum=0
    for i in L:
        lsum=lsum+i
    return lsum

def number(L):
    LV=[]
    LV.append(len(L))
    LV.append(minvalue(L))
    LV.append(maxvalue(L))
    LV.append(sumvalue(L))
    LV.append(sumvalue(L)/len(L))
    return (LV)

p=[1,2,3,4,5,6,7]
print(number(p))







