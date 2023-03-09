import sys

C, R=map(int,sys.stdin.readline().split())
num=int(sys.stdin.readline())
sheet=[[0]*C for _ in range(R)]


def One_Circle(sheet,c,r,k,cnt,m):
    for i in reversed(range(k+1,r-k)):
        sheet[i][k]=cnt
        cnt+=1
        if cnt>m:
            return cnt
    for i in range(k,c-k-1):
        sheet[k][i]=cnt
        cnt+=1
        if cnt>m:
            return cnt
    for i in range(k,r-k-1):
        sheet[i][c-k-1]=cnt
        cnt+=1
        if cnt>m:
            return cnt
    for i in reversed(range(k+1,c-k)):
        sheet[r-k-1][i]=cnt
        cnt+=1
        if cnt>m:
            return cnt
    return cnt
m=C*R
n=1
k=0
while True:
    n=One_Circle(sheet,C,R,k,n,m)
    if m<=n:
        break   
    k+=1
a,b=0,0

for i in range(R):
    for j in range(C):
        if sheet[i][j]==0:
            sheet[i][j]=m
        if sheet[i][j]==num:
            a=i
            b=j
            break

if num>m:
    print(0)
else:
    print(b+1,R-a)