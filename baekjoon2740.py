import sys

N,M =map(int, sys.stdin.readline().strip().split())

A=[]
B=[]

for _ in range(N):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    A.append(arr)

M,K =map(int, sys.stdin.readline().strip().split())
for _ in range(M):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    B.append(arr)

matrix=[[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        sum=0
        for a in range(M):
            sum+=A[i][a]*B[a][j]
        matrix[i][j]=sum
    
for i in range(N):
    for j in range(K):
        print(matrix[i][j],end=' ')
    print("")