import sys



N=int(sys.stdin.readline())
snail=[[0]*N for _ in range(N)]
num=int(sys.stdin.readline())


def MakeSnail(arr,n,k,cnt):
    for i in range(k,n-k-1):
        arr[i][k]=cnt
        cnt-=1
    for i in range(k,n-k-1):
        arr[n-k-1][i]=cnt
        cnt-=1
    for i in reversed(range(1+k,n-k)):
        arr[i][n-k-1]=cnt
        cnt-=1
    for i in reversed(range(1+k,n-k)):
        arr[k][i]=cnt
        cnt-=1

    return cnt

cnt=N*N
k=0
while True:
    cnt=MakeSnail(snail,N,k,cnt)
    if cnt==1:
        snail[N//2][N//2]=1
        break
    k+=1
a,b=0,0
for i in range(N):
    for j in range(N):
        p=snail[i][j]
        print(p,end=' ')
        if p==num:
            a=i
            b=j
    print()

print(a+1,b+1)