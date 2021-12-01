def CountRollingWindowMeasIncrease(input):
    def SumWindow(input,i_start,i_end):
        test = input[i_start:i_end]
        val = sum(test)
        #ans = input[i_end]+
        return val
    i_start = 0
    length = 3
    i_end = i_start+length
    x_last = 9999
    MeasIncCount = 0
    while i_end<=len(input):
        x = SumWindow(input,i_start,i_end)
        if x>x_last:
            MeasIncCount+=1
        x_last = x
        i_start+=1
        i_end = i_start+length
    return MeasIncCount




def CountMeasurementIncreases(input):
    x_last = 999
    MeasIncCount = 0
    for x in input:
        if x>x_last:
            MeasIncCount+=1
        x_last = x
    return MeasIncCount

def GetInput():
    with open("Week1\Day1\input.txt") as f:
        input = f.read().splitlines()
        input = list(map(int, input))
    return input

if __name__ == "__main__":
    input = GetInput()
    MeasIncCount = CountMeasurementIncreases(input)
    print("Day1Puzzle1: " + str(MeasIncCount))
    MeasIncCount = CountRollingWindowMeasIncrease(input)
    print("Day1Puzzle2: " + str(MeasIncCount))
print("Done")