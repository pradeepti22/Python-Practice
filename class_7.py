'''
#create a function that returns diff between sum of odd and sum of even numbers in a list

def diff(l):
    oddsum=0
    evensum=0
    for i in l:
        if i % 2==0:
            evensum=evensum+i
        else:
            oddsum=oddsum+i
    res=oddsum-evensum
    return res

p=[1,2,3,4]
print(diff(p))


#create a function to calc sum, avg, variance of all numbers in a list

def stats(l):
    sum=0
    mu=0
    sig2=0
    for i in l:
        sum=sum+i      
    mu=sum/len(l)

    for j in l:
        sig2=sig2+(j-mu)**2
        
    sig2/len(l)
    return (sum, mu, sig2)

p=[1,2,3,4,5,6]
print(stats(p))


#a function that accepts 2 lists and returns the product of the odd sum in the i1st list and even sum
#in the even sum in 2nd list

def listprod(l1,l2):
    evensum=0
    oddsum=0
    for i in l1:
        if i %2 == 1:
            oddsum=oddsum+i
    for j in l2:
        if j %2 == 0:
            evensum=evensum+j
    res=oddsum*evensum
    return res

p=[1,2,3,4,5,6]
q=[1,2,3,4,5,6]
print(listprod(p,q))
'''

'''Create a function courseInformation which has two parameters:
Parameter 1 is a course number.
Parameter 2 can be  ‘Room’, ‘Instructor’, or ‘Time’.
The function returns the room, instructor, or meeting time of the course specified in parameter 1.
'''

def courseInformation(N,v):
    D={'CS101': ['RM-3004', 'Prof. Haynes', '8-9:30 AM'], 
       'CS102': ['RM-4501', 'Prof. Alvarado', '9-10:30 AM'], 
       'CS103': ['RM-6775', 'Prof. Rich', '7-8:30 AM'],
       'NT110': ['RM-1244', 'Prof. Burke', '1-3 PM'],
       'CM241': ['RM-1411', 'Prof. Lee', '4-6 PM']}
    if v=='Room':
        return D[N][0]
    if v=='Instructor':
        return D[N][1]
    if v=='Time':
        return D[N][2]


print(courseInformation('CS101', 'Room'))
print(courseInformation('CS101', 'Instructor'))
print(courseInformation('CS101', 'Time'))




    
