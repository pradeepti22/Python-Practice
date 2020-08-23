import random
'''
DSFile4 = open("C:\\Users\\msgth\\Desktop\\A_Python_PACE_2020\\DataScience4",'w')

for i in range(1,101):
    DSFile4.write(str(random.randrange(1,11)) + ' ')
    if i % 10 == 0:
        DSFile4.write('\n')

DSFile4.close()

#Process a numeric file
DSFile3 = open("C:\\Users\\msgth\\Desktop\\A_Python_PACE_2020\\DataScience3",'r')

sumValues = 0;
line = DSFile3.readline()
while line != '':
    v = list(line.split())
    for i in v:
        sumValues += int(i)
    
    line = DSFile3.readline()    

DSFile3.close()


DataFile = "C:\\Users\\msgth\\Desktop\\A_Python_PACE_2020\\DataScience4"
'''
def displayFrequencyDistribution(FP):
    print('_____Frequency Distribution Chart_____')
    print()
    print('VALUE\tFREQUENCY')
    print()
    DSFile = open(FP,'r')
    NumericList = []
    FDChart = []
    values = DSFile.read()
    values = list(values.split())
    for a in values:
        NumericList.append(int(a))
    NumericList.sort()
    uniqueValues = set(NumericList)    
    for i in uniqueValues:        
        vCount = 0
        for j in NumericList:
            if j == i:
                vCount += 1
        print(str(i) + '\t' + str(vCount))               

    DSFile.close()
    print()
    print('TOTAL\t' + str(len(NumericList)))
    print('________________Prepared By HG Locklear')
    


def displayRelativeFrequencyDistribution(FP):
    print('_____Relative Frequency Distribution Chart_____')
    print()
    print('VALUE\tFREQUENCY\tRELATIVE FREQUENCY')
    print()
    Formatted = '{:.2f}'
    DSFile = open(FP,'r')
    NumericList = []
    FDChart = []
    values = DSFile.read()
    values = list(values.split())
    for a in values:
        NumericList.append(int(a))
    NumericList.sort()
    uniqueValues = set(NumericList)    
    for i in uniqueValues:        
        vCount = 0
        for j in NumericList:
            if j == i:
                vCount += 1
        print(str(i) + '\t' + str(vCount) + '\t\t'
              + str(Formatted.format(vCount/len(NumericList))))               

    DSFile.close()
    print()
    print('TOTAL\t' + str(len(NumericList)))
    print('________________Prepared By HG Locklear')
    


def displayCumulativeRelativeFrequencyDistribution(FP):
    print('_____Cumulative Relative Frequency Distribution Chart_____')
    print()
    print('VALUE\tFREQ\tRELATIVE FREQ\tCUMULATIVE RELATIVE FREQ')
    print()
    Formatted = '{:.2f}'
    DSFile = open(FP,'r')
    NumericList = []
    FDChart = []
    values = DSFile.read()
    values = list(values.split())
    for a in values:
        NumericList.append(int(a))
    NumericList.sort()
    uniqueValues = set(NumericList)
    rf = 0
    crf = 0
    for i in uniqueValues:        
        vCount = 0
        for j in NumericList:
            if j == i:                
                vCount += 1
        rf = vCount/len(NumericList)
        crf = crf + rf
        print(str(i) + '\t' + str(vCount) + '\t\t'
              + str(Formatted.format(rf))
              + '\t\t' + str(Formatted.format(crf)))               

    DSFile.close()
    print()
    print('TOTAL\t' + str(len(NumericList)))
    print('________________Prepared By HG Locklear')
    

