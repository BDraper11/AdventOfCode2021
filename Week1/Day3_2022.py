from AoC2021 import *
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)



def Puzz1(input):
    NumberEntries = len(input)
    GammaRate = ''
    EpislonRate = ''
    for idx,val in enumerate(input[0]):
        GammaRate = ''.join([GammaRate,str(int((sum([int(x[idx]) for x in input])>(NumberEntries//2))))])
        EpislonRate = ''.join([EpislonRate,str(int((sum([int(x[idx]) for x in input])<(NumberEntries//2))))])
        
    PowerCons = int(GammaRate,2)*int(EpislonRate,2)
    print("GR:\t"+GammaRate+"\t"+str(int(GammaRate,2))+"\nER:\t"+EpislonRate+"\t"+str(int(EpislonRate,2)))
    return PowerCons

def CommonalityFinder(idx,input,Dir=1,Reduce=True):
        NumberEntries = len(input)
        output = []
        if (sum([int(x[idx]) for x in input])==(NumberEntries/2)):
            if Dir==1:
                CommonalityValue = 1
            else:
                CommonalityValue = 0
        elif (sum([int(x[idx]) for x in input])>(NumberEntries/2)):
            if Dir==1:
                CommonalityValue = 1
            else:
                CommonalityValue = 0
        elif (sum([int(x[idx]) for x in input])<(NumberEntries/2)):
            if Dir==1:
                CommonalityValue = 0
            else:
                CommonalityValue = 1
        else:
            print("Error")
        for x in input:
            if Reduce and (x[idx]==str(CommonalityValue)):
                output.append(x)
        return CommonalityValue,output

def DetO2GenRating(input):
    O2GenRating = ''
    for idx,val in enumerate(input[0]):
        ret = CommonalityFinder(idx,input)
        input = ret[1]
        O2GenRating = ''.join([O2GenRating,str(ret[0])])
        if len(input)<2:
            break
    return input[0]

def DetCO2ScrubRating(input):
    CO2ScrubRating = ''
    for idx,val in enumerate(input[0]):
        ret = CommonalityFinder(idx,input,0)
        input = ret[1]
        CO2ScrubRating = ''.join([CO2ScrubRating,str(ret[0])])
        if len(input)<2:
            break
    return input[0]

def Puzz2(input):
    O2GenRating = DetO2GenRating(input)
    CO2ScrubRating = DetCO2ScrubRating(input)
    print("O2:\t"+O2GenRating+"\t"+str(int(O2GenRating,2))+"\nCO2:\t"+CO2ScrubRating+"\t"+str(int(CO2ScrubRating,2)))
    LifeSupportRating = int(O2GenRating,2)*int(CO2ScrubRating,2)
    return LifeSupportRating

if __name__ == "__main__":
    input = GetInput(1,3)
    Puzz1Ans = Puzz1(input)
    print("P1Ans: ",Puzz1Ans), pyperclip.copy(Puzz1Ans)
    Puzz2Ans = Puzz2(input)
    print("P2Ans: ",Puzz2Ans), pyperclip.copy(Puzz2Ans)