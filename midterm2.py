#Task 1: Numerical Analysis

def oddEvenValueCount(filepath):
    file=open(filepath)
    ocount = 0 #odd value count
    ecount = 0 #even values count
    parse = (file.read()).split()
    for i in parse:
        if int(i) % 2 == 0:
            ecount = ecount + 1
        else:
            ocount = ocount + 1
    return (ocount, ecount)

def statisticalAnalysis(filepath):
    file=open(filepath)
    L0 = (file.read()).split()
    L = []
    for i in L0:
        L.append(int(i))
    minV = L[0] # to find min
    for i in L:
        if i < minV:
            minV = i
    # to find max
    maxV = L[0]
    for i in L:
        if i > maxV:
            maxV = i
    #sum
    S = 0
    for i in L:
        S += i
    #range
    R = maxV - minV
    #average
    mu = S/len(L)
    #variance
    sigma2 = 0
    for i in L:
        sigma2 += (i - mu)**2
    sigma2 = sigma2 / len(L)
    sigma = (sigma2)**0.5
    return (mu, sigma2, sigma, R)

def outlierIdentification(filepath):
    file = open(filepath)
    file_numbers = (file.read()).split()
    map(int, file_numbers) # converting all elements to int type
    mean, var, SD, r = statisticalAnalysis(filepath)
    lower = int(mean - (3*SD)) # lower limit, 3 SDs away from mean
    upper = int(mean + (3*SD)) # upper limit, 3 SDs away from mean
    OList = []
    for i in file_numbers:
        if int(i) < lower: 
            OList.append(i)
        if int(i) > upper:
            OList.append(i)
    return sorted(OList)

#Task 2: Processing Functions

def countSymbols(filepath,symbol):
    file = open(filepath)
    file_symbols = (file.read()).split()
    count_symbol = 0
    for i in file_symbols:
        if i == symbol:
            count_symbol += 1
    return count_symbol

def countWords(filepath):
    file = open(filepath)
    file_symbols = (file.read()).split()
    count_words = 0
    for i in file_symbols:
        if len(i) >= 3 and i not in range(0,10):
            count_words += 1
    return count_words

#Task 3: Processing Functions

def findUnique(filepath):
    file = open(filepath)
    file_symbols = (file.read()).split()
    letters = ['A','B','C','D','E','F']
    unique_numbers = set()
    unique_letters = set()
    for i in file_symbols:
        if i in letters:
            unique_letters.add(i)
        elif int(i) in range(0,10):
            unique_numbers.add(int(i))
    return tuple(sorted(unique_numbers)), tuple(sorted(unique_letters))

def countSpecifiedWords(filepath,wordlist):
    file = open(filepath)
    file_symbols = (file.read()).split()
    dict_words = {}
    for i in wordlist:
        dict_words[i] = file_symbols.count(i)
    return dict_words

#Task 4: File Comparisons

def compareNumbers(filepath1,filepath2):
    file1 = open(filepath1)
    file2 = open(filepath2)
    file1_symbols = (file1.read()).split()
    file2_symbols = (file2.read()).split()
    file1_numbers = []
    file2_numbers = []
    comp_numbers = []
    for i in file1_symbols:
        if i.isdigit() is True:
            if int(i) in range(0,100):
                file1_numbers.append(int(i))
    for j in file2_symbols:
        if j.isdigit() is True:
            if int(j) in range(0,100):
                file2_numbers.append(int(j))
    for k in file1_numbers:
        if k not in file2_numbers:
            comp_numbers.append(k)
    return tuple(sorted(comp_numbers))

def compareWords(filepath1,filepath2):
    file1 = open(filepath1)
    file2 = open(filepath2)
    file1_symbols = (file1.read()).split()
    file2_symbols = (file2.read()).split()
    file1_words = []
    file2_words = []
    comp_words = []
    for i in file1_symbols:
        if i.isdigit() is False:
            file1_words.append(i)
    for j in file2_symbols:
        if j.isdigit() is False:
            file2_words.append(j)
    for k in file1_words:
        if k not in file2_words:
            comp_words.append(k)
    return tuple(sorted(comp_words))

#Task 5: Map Reduction & Expansion

def mapReduction(filepath1,filepath2,filepath3):
    file1 = open(filepath1)
    file2 = open(filepath2)
    file3 = open(filepath3)
    file1_words = (file1.read()).split()
    file2_words = (file2.read()).split()
    file3_words = (file3.read()).split()
    file_words = sorted(file1_words + file2_words + file3_words)
    dict_words = {}
    for i in file_words:
        dict_words[i] = file_words.count(i)
    return dict_words

def mapExpansion(filepath):
    file = open(filepath)
    file1 = open('New File 1', 'w')
    file2 = open('New File 2', 'w')
    file3 = open('New File 3', 'w')
    file_words = (file.read()).split()
    file1_words = []
    file2_words = []
    file3_words = []
    file1_alpha = ('A','B','C','D','E','F','a','b','c','d','e','f')
    file2_alpha = ('G','H','I','J','K','L','M','N','O','P','Q','R','g','h','i','j','k','l','m','n','o','p','q','r')
    file3_alpha = ('S','T','U','V','W','X','Y','Z','s','t','u','v','w','x','y','z')
    for i in file_words:
        if i.startswith(file1_alpha):
            file1_words.append(i)
        elif i.startswith(file2_alpha):
            file2_words.append(i)
        elif i.startswith(file3_alpha):
            file3_words.append(i)
    for i in sorted(set(file1_words)):
        file1.write(i)
        file1.write("\n")
    for i in sorted(set(file2_words)):
        file2.write(i)
        file2.write("\n")
    for i in sorted(set(file3_words)):
        file3.write(i)
        file3.write("\n")
    file1.close()
    file2.close()
    file3.close()
