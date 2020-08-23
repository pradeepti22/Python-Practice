#Functions

#Prob 1

#converts meters to inches
def convertToInches(m): 
    inches =(m*0.3048)*12
    return inches
print(convertToInches(12))

#Prob 2

def convertToKilometers(m): #converts miles to kms
    k=m*1.6
    print(k)
convertToKilometers(100)

#Prob 3

def fatCalories(g): #calculates grams of fat to calories
    fcal=g*9
    return(fcal)
fatCalories(10)

#Prob 4

def fatCalories(g): #calculates grams of fat to calories
    fcal=g*9
    return(fcal)
fatCalories(10)

def carCalories(g):
    ccal=g*4
    print(ccal)

def totcal(c,f):
    tcal=fatCalories(f)+ carCalories(c)
    return tcal

print(totcal(10,10))

#Prob 5

def countEvenNumbers(x):
    count=0
    for i in x:
        if i%2==0:
            count=count+1
    return(count)

l=[1,2,3,4,5,6,7,8,9,10]
print(countEvenNumbers(l))



#Prob 6

def determineMinMax(x):
    min=x[0]
    max=x[0]
    for i in x:
        if i>max:
            max=i
        elif i<min:
            min=i
    return(max,min)

l=[1,4,6,5,2,9,100]
print(determineMinMax(l))


#extra practise

#sum all values in a list


def listSum(L):
    sum=0
    for i in L:
        sum=sum+i
        return sum 


#return avg of values in a list

def listAvg(L):
    mu=listSum(L)/len(L)
    return mu



#build a model of variance - sigma square

def listSigma2(L):
    var=0
    mu=listAvg(L)
    for i in L:
        var=var+(i-mu)**2
    var=var/len(L)
    return var

def listsigma(L):
    return (listSigma2(L))**0.5


x=[1,2,3,4,5,6,7]
print(listSigma(x))

#single function to do sum,avg,var, std dev


def descriptiveStats(L):
    sum=listSum(L)
    avg=listAvg(L)
    var=listSigma2(L)
    std=listSigma(L)
    return sum, avg, var, std

descriptiveStats(x)











