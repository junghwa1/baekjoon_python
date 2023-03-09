import sys

board=[]

def countstone(a,b):
    x,y=a,b
    count=1
    while True:
        if y>17:
            break
        if board[x][y]==board[x][y+1]:
            count+=1
            y+=1
        else:
            break
    if count==5 and y<17 and board[x][y]==board[x][y+1]:
        count+=1
    if count==5 and b>0 and board[a][b]==board[a][b-1]:
        count+=1
    if count==5:
        return True
    
    x,y=a,b
    count=1
    while True:
        if x>17:
            break
        if board[x][y]==board[x+1][y]:
            count+=1
            x+=1
        else:
            break
    if count==5 and x<17 and board[x][y]==board[x+1][y]:
        count+=1
    if count==5 and a>0 and board[a][b]==board[a-1][b]:
        count+=1
    if count==5:
        return True
    

    x,y=a,b
    count=1
    while True:
        if x>17 or y>17:
            break
        if board[x][y]==board[x+1][y+1]:
            count+=1
            x+=1
            y+=1
        else:
            break
        if count==5:
            break
    if count==5 and x<17 and y<17 and board[x][y]==board[x+1][y+1]:
        count+=1
    if count==5 and a>0 and b>0 and board[a][b]==board[a-1][b-1]:
        count+=1
    if count==5:
        return True

    x,y=a,b
    count=1
    while True:
        if x<1 or y>17:
            break
        if board[x][y]==board[x-1][y+1]:
            count+=1
            x-=1
            y+=1
        else:
            break
        if count==5:
            break
    if count==5 and x>0 and y<17 and board[x][y]==board[x-1][y+1]:
        count+=1
    if count==5 and a<17 and b>0 and board[a][b]==board[a+1][b-1]:
        count+=1
    if count==5:
        return True
    
    return False

a,b=0,0
winner=0
count=1
for _ in range(19):
    board.append(list(map(int,sys.stdin.readline().strip().split())))
    
for i in range(19):
    for j in range(19):
        if board[i][j]!=0:
            if countstone(i,j):
                winner=board[i][j]
                a=i
                b=j
                break

if winner==0:
    print(winner)
else:
    print(winner)
    print(a+1,b+1)