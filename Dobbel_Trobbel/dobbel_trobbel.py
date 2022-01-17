import random

whiteDice = ['1','1','1','2','2','3']

scoreRed = ['-2',' ',' ',' ',' ',' ',' ',' ',' ',' ']
scoreBlue = [' ',' ',' ',' ',' ',' ',' ',' ',' ','-2']

list = []

def gooiFunc():
    #a = int(input("waar wil je leggen?"))
    throwBlue = random.randint(1, 6)
    throwRed = random.randint(1, 6)
    throwWhite = int(whiteDice[random.randint(0, 5)])
    list.append(throwBlue)
    list.append(throwRed)
    list.append(throwWhite)
    maxNum = max(list)
    minNum = min(list)

    optionA = throwBlue + throwRed + throwWhite
    optionB = throwBlue + throwRed - throwWhite
    optionC = throwBlue + throwRed
    optionD = maxNum - minNum
    print(list)
    print(maxNum, minNum)
    print("optie A=",optionA,"\noptie B=", optionB,"\noptie C=", optionC, "\noptie D=", optionD)
    
gooiFunc()
