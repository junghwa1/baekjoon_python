import sys

N=int(sys.stdin.readline())

arr=[]

width=0
length=0
w=False
l=False

for i in range(N):
    arr.append(input())

for i in range(N):
    w=False
    l=False
    for j in range(1,N):
        if arr[i][j-1]=='.' and arr[i][j]=='.'and w==False:
            width+=1
            w=True
        if arr[j-1][i]=='.' and arr[j][i]=='.' and l==False:
            length+=1
            l=True
        if arr[i][j-1]=='X':
            w=False
        if arr[j-1][i]=='X':
            l=False
        


print(width, length)