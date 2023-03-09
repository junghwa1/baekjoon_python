ABC=['A','B','C','D','E','F','G','H']

king, stone, N = input().split()
N=int(N)
king=list(king)
king[1]=int(king[1])
stone=list(stone)
stone[1]=int(stone[1])

def move_R():
    if king[0]==ABC[7]:
            return False
    elif king[1]==stone[1] and ABC.index(king[0])+1==ABC.index(stone[0]):
        if stone[0]=='H':
            return False
        king[0]=ABC[ABC.index(king[0])+1]
        stone[0]=ABC[ABC.index(stone[0])+1]
    else:
            king[0]=ABC[ABC.index(king[0])+1]
    return True

def move_L():
    if king[0]==ABC[0]:
            return False
    elif king[1]==stone[1] and ABC.index(king[0])-1==ABC.index(stone[0]):
        if stone[0]=='A':
            return False
        king[0]=ABC[ABC.index(king[0])-1]
        stone[0]=ABC[ABC.index(stone[0])-1]
    else:
        king[0]=ABC[ABC.index(king[0])-1]
    return True

def move_B():
    if king[1]==1:
            return False
    elif king[0]==stone[0] and king[1]-1==stone[1]:
        if stone[1]==1:
            return False
        king[1]=king[1]-1
        stone[1]=stone[1]-1
    else:
        king[1]=king[1]-1
    return True

def move_T():
    if king[1]==8:
            return False
    elif king[0]==stone[0] and king[1]+1==stone[1]:
        if stone[1]==8:
            return False
        king[1]=king[1]+1
        stone[1]=stone[1]+1
    else:
        king[1]=king[1]+1
    return True


for _ in range(N):
    commend=input()
    if commend=='R':
        move_R()
    elif commend=='L':
        move_L()
    elif commend=='B':
        move_B()
    elif commend=='T':
        move_T()
    elif commend=='RT':
        if king[1]==8 or king[0]==ABC[7]:
            continue
        elif king[1]+1==stone[1] and ABC.index(king[0])+1==ABC.index(stone[0]):
            if stone[0]=='H' or stone[1]==8:
                continue
            king[0]=ABC[ABC.index(king[0])+1]
            stone[0]=ABC[ABC.index(stone[0])+1]
            king[1]=king[1]+1
            stone[1]=stone[1]+1
        else:
            king[0]=ABC[ABC.index(king[0])+1]
            king[1]=king[1]+1   
                
    elif commend=='LT':
        if king[1]==8 or king[0]==ABC[0]:
            continue
        elif king[1]+1==stone[1] and ABC.index(king[0])-1==ABC.index(stone[0]):
            if stone[0]=='A' or stone[1]==8:
                continue
            king[0]=ABC[ABC.index(king[0])-1]
            stone[0]=ABC[ABC.index(stone[0])-1]
            king[1]=king[1]+1
            stone[1]=stone[1]+1
        else:
            king[0]=ABC[ABC.index(king[0])-1]
            king[1]=king[1]+1
    elif commend=='RB':
        if king[1]==1 or king[0]==ABC[7]:
            continue
        elif king[1]-1==stone[1] and ABC.index(king[0])+1==ABC.index(stone[0]):
            if stone[0]=='H' or stone[1]==1:
                continue
            king[0]=ABC[ABC.index(king[0])+1]
            stone[0]=ABC[ABC.index(stone[0])+1]
            king[1]=king[1]-1
            stone[1]=stone[1]-1
        else:
            king[0]=ABC[ABC.index(king[0])+1]
            king[1]=king[1]-1
    elif commend=='LB':
        if king[1]==1 or king[0]==ABC[0]:
            continue
        elif king[1]-1==stone[1] and ABC.index(king[0])-1==ABC.index(stone[0]):
            if stone[0]=='A' or stone[1]==1:
                continue
            king[0]=ABC[ABC.index(king[0])-1]
            stone[0]=ABC[ABC.index(stone[0])-1]
            king[1]=king[1]-1
            stone[1]=stone[1]-1
        else:
            king[0]=ABC[ABC.index(king[0])-1]
            king[1]=king[1]-1

print(king[0]+str(king[1]))
print(stone[0]+str(stone[1]))