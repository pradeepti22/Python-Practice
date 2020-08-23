#MIDTERM EXAM

#Task 1: Numerical Modification Functions

def oddValueList(l):
    new=list()
    for i in l:
        if l[i]%2==1:
            new.append(i)
    print(new)


def evenValueList(l):
    new=list()
    for i in l:
        if l[i]%2==0:
            new.append(i)
    print(new)


def reciprocalList(l):
    new=list()
    for i in l:
        i=1/i
        new.append(i)
    print(new)



#Task 2: Statistical Analysis Functions

def muValue(l):
    odd_sum=0
    odd_count=0
    even_sum=0
    even_count=0
    oavg=0
    eavg=0
    i=0

    while i < len(l):
        
        if l[i] %2==0:
            even_sum=even_sum+l[i]
            even_count=even_count+1
            i=i+1
            
        else:
            odd_sum=odd_sum+l[i]
            odd_count=odd_count+1
            i=i+1

    oavg=odd_sum/odd_count
    eavg=even_sum/even_count
    return(oavg, eavg)


def sigma2Value(l):
    odd_sum=0
    odd_count=0
    even_sum=0
    even_count=0
    oavg=0
    eavg=0
    evar=0
    ovar=0
    fevar=0
    fovar=0
    i=0

    while i < len(l):
        
        if l[i] %2==0:
            even_sum=even_sum+l[i]
            even_count=even_count+1
            eavg=even_sum/even_count
            evar=evar+(i-eavg)**2
            i=i+1
            
        else:
            odd_sum=odd_sum+l[i]
            odd_count=odd_count+1
            oavg=odd_sum/odd_count
            ovar=ovar+(i-oavg)**2
            i=i+1
    
    fevar=evar/even_count
    fovar=ovar/odd_count
    return(fevar, fovar)


def sigmaValue(l):
    odd_sum=0
    odd_count=0
    even_sum=0
    even_count=0
    oavg=0
    eavg=0
    evar=0
    ovar=0
    fevar=0
    fovar=0
    esd=0
    osd=0
    i=0

    while i < len(l):
        
        if l[i] %2==0:
            even_sum=even_sum+l[i]
            even_count=even_count+1
            eavg=even_sum/even_count
            evar=evar+(i-eavg)**2
            i=i+1
            
        else:
            odd_sum=odd_sum+l[i]
            odd_count=odd_count+1
            oavg=odd_sum/odd_count
            ovar=ovar+(i-oavg)**2
            i=i+1
    
    fevar=evar/even_count
    fovar=ovar/odd_count
    esd=(fevar)**0.5
    osd=(fovar)**0.5
    return(esd,osd)



def numericalAnalysis(l):
    def ecount(l):
        ec=0
        for i in l:
            if i%2==0:
                ec=ec+1
        return(ec)

    def ocount(l):
        oc=0
        for i in l:
            if i%2==1:
                oc=oc+1
        return(oc)
        
    def oddValueList(l):
        new=list()
        for i in l:
            if l[i]%2==1:
                new.append(i)
        return(new)


    def evenValueList(l):
        new=list()
        for i in l:
            if l[i]%2==0:
                new.append(i)
        return(new)

    c,d=muValue(l)
    e,f=sigma2Value(l)
    g,h=sigmaValue(l)

    print('NUMERICAL ANALYSIS REPORT________________________________CREATED BY PRADEEPTI UPADHYAYULA\n')
    print('Total Numbers\tEvens\tOdds\tMu-Even\tMu-Odd\tSigma2-Even\tSigma2-Odd\tSigma-Even\tSigma-Odd')
    print(len(l),'\t',ecount(l),'\t',int(ocount(l)),'\t',format(c, '.2f'),'\t',format(d, '.2f'),'\t\t',format(e, '.2f'),'\t\t',format(f, '.2f'),'\t\t',format(g, '.2f'),'\t\t',format(h, '.2f'),'\n')
        


a=[1,11,3,14,5,15,7,18,9,20]
b=list(range(77))
c=list(range(62))

numericalAnalysis(a)

numericalAnalysis(b)

numericalAnalysis(c)














    
