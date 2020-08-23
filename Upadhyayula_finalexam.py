class VirusDetector:
    detectorCount=0

    def __init__(self, detectorID, detectorVersion, detectorPassword):
        self.detectorID = detectorID
        self.detectorVersion = detectorVersion
        self.detectorPassword = detectorPassword
        self.analyzedFile = None
        self.codeBuffer = None
        VirusDetector.detectorCount += 1

    def displayDetectorInfo(self):
        info = "______VIRUS DETECTOR ID: Locklear-1______" + "\n" + "DETECTOR VERSION: " + self.detectorVersion + "\n" + "DETECTOR PASSWORD: " + self.detectorPassword + "\n"
        return info

    def readFileToCodeBuffer(self, filepath):
        self.analyzedFile = "Current File in Buffer:" + filepath
        file = open(filepath)
        self.codeBuffer = file.read()
        return self.analyzedFile

    def flushCodeBuffer(self):
        self.codeBuffer = None

    def analyzeCodeBuffer(self):
        print(self.displayDetectorInfo(), end = '')
        print(self.analyzedFile)
        print("________________ANALYSIS_________________")
        print("Total Bytes: ", self.countTotalBytes(), "\t", "Total Bits: ", self.countTotalBits(), "\t", "True Bits: ", self.countTrueBits(), "\t", "False Bits: ", self.countFalseBits())
        print("True Bytes: ", self.countTrueBytes(), "\t", "False Bytes: ", self.countFalseBytes())
        print("All True Bytes: ", self.countAllTrueBytes(), "\t", "All False Bytes: ", self.countAllFalseBytes())
        print("*******************************************")
        print("Recurrent True Bytes: ", self.countRecurrentTrueBytes(), "\t", "Recurrent False Bytes: ", self.countRecurrentFalseBytes(), "\t", "Symmetric Bytes: ", self.countSymmetricBytes())
        print("*******************************************")
        TrueBitPercentage = format(((self.countTrueBits()*100) / self.countTotalBits()), '.2f')
        FalseBitPercentage = format(((self.countFalseBits()*100) / self.countTotalBits()), '.2f')
        TrueBytePercentage = format(((self.countTrueBytes()*100) / self.countTotalBytes()), '.2f')
        AllTrueBytesPercentage = format(((self.countAllTrueBytes()*100) / self.countTotalBytes()), '.2f')
        RecurrentTrueBytesPercentage = format(((self.countRecurrentTrueBytes()*100) / self.countTotalBytes()), '.2f')
        FalseBytePercentage = format(((self.countFalseBytes()*100) / self.countTotalBytes()), '.2f')
        AllFalseBytesPercentage = format(((self.countAllFalseBytes()*100) / self.countTotalBytes()), '.2f')
        RecurrentFalseBytesPercentage = format(((self.countRecurrentFalseBytes()*100) / self.countTotalBytes()), '.2f')
        SymmetricBytePercentage = format(((self.countSymmetricBytes()*100) / self.countTotalBytes()), '.2f')
        print("True Bit Percentage: ", TrueBitPercentage, '%', "\t", "False Bit Percentage: ", FalseBitPercentage, '%')
        print("True Byte Percentage: ", TrueBytePercentage, '%', "\t", "False Byte Percentage: ", FalseBytePercentage, '%')
        print()
        print("All True Byte Percentage: ", AllTrueBytesPercentage, '%', "\t", "All False Byte Percentage: ", AllFalseBytesPercentage, '%')
        print("Recurrent True Byte Percentage: ", RecurrentTrueBytesPercentage, '%', "\t", "Recurrent False Byte Percentage: ", RecurrentFalseBytesPercentage, '%')
        print("Symmetric Byte Percentage: ", SymmetricBytePercentage, '%')
        print("###########################################################")
        MalformedByteCount = self.checkForMalformedByte()
        print("Malformed Byte Count: ", MalformedByteCount[0])
        print("Malformed Byte(s) are located at Code Buffer Index(es): ", MalformedByteCount[1])
        print("^^^^^^^^^^^^^^^^^VIRUS DETECTION RESULTS^^^^^^^^^^^^^^^^^^^")
        if self.detectAlphaVirus() == True:
            print("Alpha Virus: Alpha Virus HAS BEEN Detected")
        else:
            print("Alpha Virus: Alpha Virus NOT Detected")

        if self.detectBetaVirus() == True:
            print("Beta Virus: Beta Virus HAS BEEN Detected")
        else:
            print("Beta Virus: Beta Virus NOT Detected")

        if self.detectGammaVirus() == True:
            print("Gamma Virus: Gamma Virus HAS BEEN Detected")
        else:
            print("Gamma Virus: Gamma Virus NOT Detected")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    def countTotalBytes(self):
        bytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            bytecount += 1
        return int(bytecount)

    def countTotalBits(self):
        bitcount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            for j in i:
                bitcount += 1
        return bitcount

    def countTrueBits(self):
        tbitcount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            for j in i:
                if int(j) == 1:
                    tbitcount += 1
        return tbitcount

    def countFalseBits(self):
        fbitcount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            for j in i:
                if int(j) == 0:
                    fbitcount += 1
        return fbitcount

    def countTrueBytes(self):
        tbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            tbitcount = 0
            fbitcount = 0
            if len(i) == 8:
                for j in i:
                    if int(j) == 1:
                        tbitcount += 1
                    else:
                        fbitcount += 1
            if tbitcount > fbitcount:
                tbytecount += 1
        return tbytecount

    def countFalseBytes(self):
        fbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            tbitcount = 0
            fbitcount = 0
            if len(i) == 8:
                for j in i:
                    if int(j) == 0:
                        fbitcount += 1
                    else:
                        tbitcount += 1
            if fbitcount >= tbitcount:
                fbytecount += 1
        return fbytecount

    def countAllTrueBytes(self):
        atbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if i == '11111111':
                atbytecount += 1
        return atbytecount

    def countAllFalseBytes(self):
        afbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if i == '00000000':
                afbytecount += 1
        return afbytecount

    def countRecurrentTrueBytes(self):
        rtbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if i == '10101010':
                rtbytecount += 1
        return rtbytecount

    def countRecurrentFalseBytes(self):
        rfbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if i == '01010101':
                rfbytecount += 1
        return rfbytecount

    def countSymmetricBytes(self):
        sbytecount = 0
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if i == '11110000' or i == '00001111':
                sbytecount += 1
        return sbytecount

    def checkForMalformedByte(self):
        mbytecount = 0
        mlist = []
        codeBuffer = (self.codeBuffer).split()
        for i in codeBuffer:
            if len(i) != 8:
                mbytecount += 1
                mlist.append(codeBuffer.index(i))
        return (mbytecount,mlist)

    def checkTrueBit(self, b):
        for i in b:
            if i == '1':
                return True
            else:
                return False

    def detectAlphaVirus(self):
        C1 = self.countRecurrentTrueBytes()
        C2 = self.countAllTrueBytes()
        C3 = self.countAllTrueBytes()
        C4 = self.countTotalBits()
        CU = self.checkForMalformedByte()
        if CU[0] != 0:
            if (C1 > 6) or (C2 >= 1) or (C3 > 4) or (C4%6 == 0):
                return True
            else:
                return False
        else:
            return False

    def detectBetaVirus(self):
        C1 = self.countRecurrentTrueBytes()
        C2 = self.countAllFalseBytes()
        C3 = self.countSymmetricBytes()
        C4 = self.countTotalBits()
        CU = self.checkForMalformedByte()
        if CU[0] > 6:
            if (C1 == 0) or (C2 > 0) or (C3 > 4) or (C4%3 == 0):
                return True
            else:
                return False
        else:
            return False

    def detectGammaVirus(self):
        C1 = self.countRecurrentFalseBytes()
        C2 = self.checkForMalformedByte()
        C3_1 = self.countRecurrentTrueBytes()
        C3_2 = self.countSymmetricBytes()
        C4_1 = self.countTrueBytes()
        C4_2 = self.countFalseBytes()
        if (C1 == 8) or (C2[0] > 0) or ((C3_1 > 0) or (C3_2 > 0)) or (C4_1 > (0.08 * C4_2)):
            return True
        else:
            return False

    @staticmethod
    def displayDetectorCodeBuffer(V):
        if V.codeBuffer is None:
            return "Buffer for Virus Detector Locklear-1 is empty"
        else:
            return V.codeBuffer

#MAIN Function Definition
def main():
    # F = 'C:\\Users\\msgth\\Desktop\\A_Python_PACE\\Ifile1'
    # G = 'C:\\Users\\msgth\\Desktop\\A_Python_PACE\\Ifile2'
    F = 'V:\\Coursera\\Python Specialization\\Deepu_Quiz\\Ifile1'
    G = 'V:\\Coursera\\Python Specialization\\Deepu_Quiz\\Ifile2'

    V = VirusDetector('Locklear-1', 'Lock-A', 'Gene')
    V.readFileToCodeBuffer(F)
    V.analyzeCodeBuffer()
    V.flushCodeBuffer()

    V.readFileToCodeBuffer(G)
    V.analyzeCodeBuffer()
    V.flushCodeBuffer()
    print(VirusDetector.displayDetectorCodeBuffer(V))

main()
