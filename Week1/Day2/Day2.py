import pandas as pd
def Puzz1(dir,mag):
    Puzz1Ans = []
    horizCount = 0
    vertiCount = 0
    for idx, val in enumerate(dir):
        if val == "forward":
            horizCount+=mag[idx]
        elif val == "down":
            vertiCount+=mag[idx]
        elif val == "up":
            vertiCount-=mag[idx]
    Puzz1Ans = horizCount*vertiCount
    return Puzz1Ans

def Puzz2(dir,mag):
    Puzz2Ans = []
    horizCount = 0
    aim = 0
    vertiCount = 0
    for idx, val in enumerate(dir):
        if val == "forward":
            horizCount+=mag[idx]
            vertiCount+=mag[idx]*aim
        elif val == "down":
            aim+=mag[idx]
        elif val == "up":
            aim-=mag[idx]
    Puzz2Ans = horizCount*vertiCount
    return Puzz2Ans


def GetInput():
    with open("Week1\Day2\input.txt") as f:
        input = f.read().splitlines()
        output = []
        for line in input:
            output.append(line.split())
        dir = [i[0] for i in output]
        mag = [i[1] for i in output]
        mag = list(map(int,mag))
        df = pd.DataFrame({"Direction": dir,"Magnitude": mag})
    return input, dir, mag, df

if __name__ == "__main__":
    input, dir, mag, df = GetInput()
    Puzz1Ans = Puzz1(dir,mag)
    print("Puzzle1: " + str(Puzz1Ans))
    Puzz2Ans = Puzz2(dir,mag)
    print("Puzzle2: " + str(Puzz2Ans))
print("Done")