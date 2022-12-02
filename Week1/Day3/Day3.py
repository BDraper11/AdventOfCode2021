import pandas as pd

def ProcessInput(input):
    for b in range(len(input[0])):
        if 'df' not in locals():
            df = pd.DataFrame({"Bit"+str(b) : [int(i[b]) for i in input]})
        else:
            df_new = pd.DataFrame({"Bit"+str(b) : [int(i[b]) for i in input]})
            df = df.join(df_new)
        
    df_dfstats = df.apply(pd.value_counts)

    return df, df_dfstats
def GetGammaRate(df):
    df_dfstats = df.apply(pd.value_counts)
    gamma_rate = df_dfstats.idxmax().to_list()
    gamma_rate = map(str,gamma_rate)
    gamma_rate =''.join(gamma_rate)
    gamma_rate = int(gamma_rate,2)
    gamma_rate = format(gamma_rate,'012b')
    #print(gamma_rate,"\t\t--->\t\t",int(gamma_rate,2))
    return gamma_rate
def GetEpsilonRate(df):
    df_dfstats = df.apply(pd.value_counts)
    epsilon_rate = df_dfstats.idxmin().to_list()
    epsilon_rate = map(str,epsilon_rate)
    epsilon_rate =''.join(epsilon_rate)
    epsilon_rate = int(epsilon_rate,2)
    epsilon_rate = format(epsilon_rate,'012b')
    #print(epsilon_rate,"\t\t--->\t\t",int(epsilon_rate,2))
    return epsilon_rate
def Puzz1(df_dfstats):
    Puzz1Ans = []
    gamma_rate = df_dfstats.idxmax().to_list()
    gamma_rate = map(str,gamma_rate)
    gamma_rate =''.join(gamma_rate)
    gamma_rate = int(gamma_rate,2)
    XOR_base = 2**len(input[0])-1
    epsilon_rate = gamma_rate^XOR_base

    Puzz1Ans = gamma_rate*epsilon_rate
    return Puzz1Ans, gamma_rate, epsilon_rate
def Puzz2(df,gamma_rate, epsilon_rate):
    Puzz2Ans = []
    def O2GenRat(df,gamma_rate):
        df_loc = df

        for bit,_ in enumerate(format(gamma_rate,'012b')):
            gamma_rate = GetGammaRate(df_loc)
            val = gamma_rate[bit]
            val = int(val)
            #print("Bit = ",bit)
            #print("Val = ",val)

            #print(df_loc.apply(pd.value_counts))
            df_dfstats = df_loc.apply(pd.value_counts)

            if bit == 0:
                df_loc = df_loc.drop(df_loc[df_loc.Bit0 != val].index)
            elif bit == 1:
                df_loc = df_loc.drop(df_loc[df_loc.Bit1 != val].index)
            elif bit == 2:
                df_loc = df_loc.drop(df_loc[df_loc.Bit2 != val].index)
            elif bit == 3:
                df_loc = df_loc.drop(df_loc[df_loc.Bit3 != val].index)
            elif bit == 4:
                df_loc = df_loc.drop(df_loc[df_loc.Bit4 != val].index)
            elif bit == 5:
                df_loc = df_loc.drop(df_loc[df_loc.Bit5 != val].index)
            elif bit == 6:
                df_loc = df_loc.drop(df_loc[df_loc.Bit6 != val].index)
            elif bit == 7:
                df_loc = df_loc.drop(df_loc[df_loc.Bit7 != val].index)
            elif bit == 8:
                df_loc = df_loc.drop(df_loc[df_loc.Bit8 != val].index)
            elif bit == 9:
                df_loc = df_loc.drop(df_loc[df_loc.Bit9 != val].index)
            elif bit == 10:
                df_loc = df_loc.drop(df_loc[df_loc.Bit10 != val].index)
            elif bit == 11:
                df_loc = df_loc.drop(df_loc[df_loc.Bit11 != val].index)
            else:
                print("Oh dear")
                break

            #print("df");print(df_loc)
        gamma_rate = GetGammaRate(df_loc)
        #print(gamma_rate)
        #print(int(gamma_rate,2))
        O2GenR = int(gamma_rate,2)
        return O2GenR
    def CO2ScrubRat(df,epsilon_rate):
        df_loc = df

        for bit,_ in enumerate(format(epsilon_rate,'012b')):
            epsilon_rate = GetEpsilonRate(df_loc)
            val = epsilon_rate[bit]
            val = int(val)
            #print("Bit = ",bit)
            #print("Val = ",val)

            #print(df_loc.apply(pd.value_counts))
            df_dfstats = df_loc.apply(pd.value_counts)

            if bit == 0:
                df_loc = df_loc.drop(df_loc[df_loc.Bit0 != val].index)
            elif bit == 1:
                df_loc = df_loc.drop(df_loc[df_loc.Bit1 != val].index)
            elif bit == 2:
                df_loc = df_loc.drop(df_loc[df_loc.Bit2 != val].index)
            elif bit == 3:
                df_loc = df_loc.drop(df_loc[df_loc.Bit3 != val].index)
            elif bit == 4:
                df_loc = df_loc.drop(df_loc[df_loc.Bit4 != val].index)
            elif bit == 5:
                df_loc = df_loc.drop(df_loc[df_loc.Bit5 != val].index)
            elif bit == 6:
                df_loc = df_loc.drop(df_loc[df_loc.Bit6 != val].index)
            elif bit == 7:
                df_loc = df_loc.drop(df_loc[df_loc.Bit7 != val].index)
            elif bit == 8:
                df_loc = df_loc.drop(df_loc[df_loc.Bit8 != val].index)
            elif bit == 9:
                df_loc = df_loc.drop(df_loc[df_loc.Bit9 != val].index)
            elif bit == 10:
                df_loc = df_loc.drop(df_loc[df_loc.Bit10 != val].index)
            elif bit == 11:
                df_loc = df_loc.drop(df_loc[df_loc.Bit11 != val].index)
            else:
                print("Oh dear")
                break

            #print("df");print(df_loc)
        gamma_rate = GetGammaRate(df_loc)
        #print(gamma_rate)
        #print(int(gamma_rate,2))
        CO2ScrubR = int(gamma_rate,2)
        return CO2ScrubR
    
    O2GenR = O2GenRat(df,gamma_rate)
    CO2ScrubR = CO2ScrubRat(df,epsilon_rate)

    Puzz2Ans = O2GenR*CO2ScrubR
    return Puzz2Ans
def GetInput():
    with open("Week1\Day3\input.txt") as f:
        input = f.read().splitlines()
        #print(str(len(input[0]))+"/t"+str(2**12))
    return input

if __name__ == "__main__":
    input = GetInput()
    df, df_dfstats = ProcessInput(input)
    Puzz1Ans, gamma_rate, epsilon_rate = Puzz1(df_dfstats)
    print("Puzzle1:\t\t" + str(Puzz1Ans))
    print("Gamma:\t\t\t" + format(gamma_rate,'012b'))
    print("Epsilon:\t\t" + format(epsilon_rate,'012b'))
    Puzz2Ans = Puzz2(df,gamma_rate, epsilon_rate)
    print("Puzzle2:\t\t" + str(Puzz2Ans))
print("Done")