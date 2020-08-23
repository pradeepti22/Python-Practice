#numeric models

import LocklearStats as genepy

Apples=[['Red', 3, 5.1], ['Redish', 3.6, 5], ['RedYellow', 3.9, 5.15], ['Red', 3,9, 5.15], ['Red', 3.7, 5], ['Red', 3.5, 5.7]]

def normalizeDataValues(D):
        DataList = []
        for i in D:
            NL = []
            if i[0] == 'Red':
                NL.append(1)
            if i[0] != 'Red':
                NL.append(2)
            NL.append(i[1])
            NL.append(i[2])
            DataList.append(NL)
        return DataList

print(normalizeDataValues(Apples))

def buildTemplate(D):
        Y = normalizeDataValues(D)
        F1 = []; F2 = []; F3 = []
        T = []
        for i in Y:
            F1. append(i[0])
            F2. append(i[1])
            F3. append(i[2])
        a = genepy.avgList(F1)
        b = genepy.avgList(F2)
        c = genepy.avgList(F3)
        T = [a,b,c]
        return T

print(buildTemplate(Apples))
