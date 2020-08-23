def minList(L):
    minV = L[0]
    for i in L:
        if i < minV:
            minV = i
    return minV

def maxList(L):
    maxV = L[0]
    for i in L:
        if i > maxV:
            maxV = i
    return maxV

def sumList(L):
    S = 0
    for i in L:
        S += i
    return S

def productList(L):
    S = 0
    for i in L:
        S += i
    return S

def rangeList(L):
    R = maxList(L) - minList(L)
    return R

def percentileList(P,L):
    L.sort()
    if len(L) % 2 == 0:
        pv = int((P/100) * len(L))
        pv = pv - 1
    else:
        pv = int((P/100) * len(L))
    return L[pv]

def firstQuartileList(L):
    return percentileList(25,L)

def secondQuartileList(L):
    return percentileList(50,L)

def thirdQuartileList(L):
    return percentileList(75,L)

def interquartileRangeList(L):
    IQR = percentileList(75,L) - percentileList(25,L)
    return IQR

def midrangeList(L):
    MR = (maxList(L) + minList(L)) / 2
    return MR

def avgList(L):
    mu = sumList(L) / len(L)
    return mu

def medianList(L):
    sortedL = L.sort()    
    if len(L) % 2 == 0:
        index = int(0.5 * len(L))
        median = (L[index - 1] + L[index]) / 2
    else:
        index = int(0.5 * len(L))
        median = L[index]
    return median

def varianceList(L):
    sigma2 = 0
    mu = avgList(L)
    for i in L:
        sigma2 += (i - mu)**2
    sigma2 = sigma2 / len(L)
    return sigma2

def standardDeviationList(L):
    sigma = varianceList(L)**0.5
    return sigma

def modeList(L):
    L.sort()
    uniqueValues = set(L)
    cValue = L[0]
    cCount = 0
    for i in uniqueValues:         
        vCount = 0
        for j in L:
            if i == j:
                vCount += 1
        if vCount > cCount:
            cValue = i
            cCount = vCount
    return cValue

def coefficientOfVariation(L):
    CV = standardDeviation(L) / meanList(L)
    return CV

def outlierList(L):
    IQR = interquartileRangeList(L)
    LowerLimit = firstQuartileList(L) - (1.5 *IQR)
    UpperLimit = thirdQuartileList(L) + (1.5 *IQR)
    OList = []
    for i in L:
        if i < LowerLimit:
            OList.append(i)
        if i > UpperLimit:
            OList.append(i)
    OList.sort()
    return OList

def standardNormalizeList(L):
    mu = avgList(L)
    sigma = standardDeviationList(L)
    NormList = []
    for i in L:
        norm = (i - mu) / sigma
        NormList.append(norm)
    return NormList

def unityNormalizeList(L):
    minV = minList(L)
    maxV = maxList(L)
    NormList = []
    for i in L:
        norm = (i - minV) / (maxV - minV)
        NormList.append(norm)
    return NormList

def featureScaleList(L,a,b):
    minV = minList(L)
    maxV = maxList(L)
    NormList = []
    for i in L:
        norm = a + ((i - minV)*(b-a) / (maxV - minV))
        NormList.append(norm)
    return NormList
    
        

def formatFloatList(L,DP):
    Formatted = '{:.'+str(DP)+'}'
    NL = []
    for i in L:
       NL.append(Formatted.format(i))
    return NL
        


    



  
