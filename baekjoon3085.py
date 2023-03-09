import sys
import copy
N=int(sys.stdin.readline())

isMax=False
board=[]
result=0
answer=0
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

origin=[]

origin.extend(board)
tmp=''

def widthCountColor(board,N,k):
    max_count=0
    for i in range(0,N):
        count=1
        for j in range(1,N):
            if board[j-1][i]==board[j][i]:
                count+=1
            else:
                count=1
            if max_count<count:
                max_count=count
            if max_count==N:
                return N
    count=1
    for i in range(1,N):
        if board[k][i-1]==board[k][i]:
            count+=1
        else:
            count=1
        if max_count<count:
            max_count=count
        if max_count==N:
            return N
    return max_count

def lengthCountColor(board,N,k):
    max_count=0
    for i in range(0,N):
        count=1
        for j in range(1,N):
            if board[i][j-1]==board[i][j]:
                count+=1
            else:
                count=1
            if max_count<count:
                max_count=count
            if max_count==N:
                return N
    count=1
    for i in range(1,N):
        if board[i-1][k]==board[i][k]:
            count+=1
        else:
            count=1
        if max_count<count:
            max_count=count
        if max_count==N:
            return N

    return max_count

result=widthCountColor(board,N,0)
if result>answer:
    answer=result
result=lengthCountColor(board,N,0)
if result>answer:
    answer=result

for i in range(0,N):
    for j in range(1,N):
        board=[]
        board=copy.deepcopy(origin)
        tmp=board[i][j-1]
        board[i][j-1]=board[i][j]
        board[i][j]=tmp
        result=widthCountColor(board,N,i)
        if result==N:
            answer=N
            isMax=True
            break
        if result>answer:
            answer=result 
    if isMax==True:
        break

for i in range(0,N):
    if isMax==True:
        break
    for j in range(1,N):
        board=[]
        board=copy.deepcopy(origin)
        tmp=board[j-1][i]
        board[j-1][i]=board[j][i]
        board[j][i]=tmp
        result=lengthCountColor(board,N,i)
        if result==N:
            answer=N
            isMax=True
            break
        if result>answer:
            answer=result
    if isMax==True:
        break

print(answer)