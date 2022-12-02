class Board():
    def __init__(self,boardlines):
        def GetAllWinVectors(boardlines):
            winVectors = []
            x = boardlines.split('\n')
            for r in x:
                t = [int(s) for s in r.split() if s.isdigit()]
                winVectors.append(t)
            for idx in range(len(winVectors[0:5])):
                new_winV = [winV[idx] for winV in winVectors[0:5]]
                winVectors.append(new_winV)
            return winVectors
        self.WinVectors = GetAllWinVectors(boardlines)
    def CheckForBoardWin(self,calledNumbers):
        for thisWinVector in self.WinVectors:
            if all(elem in calledNumbers for elem in thisWinVector):
                return True, thisWinVector
        return False, []
    def GetUnmarkedNumbers(self,calledNumbers):
        allBoardNumbers=[]
        [allBoardNumbers.append(i) for x in self.WinVectors[0:5] for i in x]
        unmarkedNumbers = list(set(allBoardNumbers) - set(calledNumbers))
        return unmarkedNumbers

def CheckForWin(Boards,calledNumbers):
    for Board in Boards:
        status, WinningWinVector = Board.CheckForBoardWin(calledNumbers)
        if status:
            winBoardIndex = Boards.index(Board)
            #print(winBoardIndex)
            return True, sum(Board.GetUnmarkedNumbers(calledNumbers)), winBoardIndex
    return False,[],[]

def ProcessInput(input):
    input_loc = input
    ProcInput = []
    for lidx, line in enumerate(input_loc):
        if "," in line:
            calls = line.split(",")
            input.pop(lidx)
    ProcInput = input
    return ProcInput, calls

def GetBoards(ProcInput):
    ProcInput_loc = ProcInput
    lineCounter = 0
    Boards = []
    while len(ProcInput_loc) != 0:
        boardlines = ProcInput_loc[0]
        Boards.append(Board(boardlines))
        ProcInput_loc = ProcInput_loc[1:]    
    return Boards

def Puzz1(Boards,calls):
    Puzz1Ans = []
    calledNumbers = []
    for number in calls:
        number = int(number)
        if (len(calledNumbers)>=5):
            status, sumOfUnmarkedNumbers, winBoardIndex = CheckForWin(Boards,calledNumbers)
            if status:
                factor = calledNumbers[-1]
                return sumOfUnmarkedNumbers*factor
        calledNumbers.append(number)
    return Puzz1Ans
def Puzz2(Boards,calls):
    Puzz2Ans = []
    listOfBoards = list(range(len(Boards)))
    calledNumbers = []
    while len(listOfBoards)>1 and len(calledNumbers) != len(calls):
        print("Num Boards:\t\t",len(listOfBoards))
        for number in calls:
            number = int(number)
            if (len(calledNumbers)>=5):
                status, sumOfUnmarkedNumbers, winBoardIndex = CheckForWin(Boards,calledNumbers)
                if status:
                    #print(winBoardIndex)
                    try:
                        listOfBoards.remove(winBoardIndex)
                    except:
                        pass
                    factor = calledNumbers[-1]
            calledNumbers.append(number)
    Puzz2Ans = sumOfUnmarkedNumbers*factor
    return Puzz2Ans
def GetInput():
    with open("Week1\Day4\inputDemo.txt") as f:
        input = f.read().split("\n\n")
    return input

if __name__ == "__main__":
    input = GetInput()
    ProcInput, calls = ProcessInput(input)
    Boards = GetBoards(ProcInput)
    Puzz1Ans = Puzz1(Boards, calls)
    print("Puzzle1:\t\t" + str(Puzz1Ans))
    Puzz2Ans = Puzz2(Boards,calls)
    print("Puzzle2:\t\t" + str(Puzz2Ans))
print("Done")