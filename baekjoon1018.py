from sys import stdin

input=stdin.readline

def check_board(a,b):
    cnt1=0
    cnt2=0
    Black_and_White='B'
    for i in range(a,a+8):
        for j in range(b,b+8):
            if Black_and_White!=board[i][j]:
                cnt1+=1
            if Black_and_White=='W':
                Black_and_White='B'
            else:
                Black_and_White='W'
        if Black_and_White=='W':
            Black_and_White='B'
        else:
            Black_and_White='W'
    
    Black_and_White='W'
    for i in range(a,a+8):
        for j in range(b,b+8):
            if Black_and_White!=board[i][j]:
                cnt2+=1
            if Black_and_White=='W':
                Black_and_White='B'
            else:
                Black_and_White='W'
        if Black_and_White=='W':
            Black_and_White='B'
        else:
            Black_and_White='W'
    return min(cnt1,cnt2)

N, M= map(int,input().split())

board=[]
cnt=0
black=True

Min=64
for i in range(N):
    arr=input().strip()
    arr=list(arr)
    board.append(list(arr))


for i in range(0,N-7):
    for j in range(0,M-7):
        cnt=check_board(i,j)
        if Min>cnt:
            Min=cnt

print(Min)