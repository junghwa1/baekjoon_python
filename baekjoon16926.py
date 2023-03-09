import sys

def turnMatrix(matrix,n,m,r,k):
    arr=[]
    for i in range(k,n-1-k):
        arr.append(matrix[i][k])
    for i in range(k,m-1-k):
        arr.append(matrix[n-1-k][i])
    for i in reversed(range(1+k,n-k)):
        arr.append(matrix[i][m-1-k])
    for i in reversed(range(1+k,m-k)):
        arr.append(matrix[k][i])
    
    for i in range(r):
        tmp=arr[-1]
        del arr[-1]
        arr.insert(0,tmp)
    j=0
    for i in range(k,n-1-k):
        matrix[i][k]=arr[j]
        j+=1
    for i in range(k,m-1-k):
        matrix[n-1-k][i]=arr[j]
        j+=1
    for i in reversed(range(1+k,n-k)):
        matrix[i][m-1-k]=arr[j]
        j+=1
    for i in reversed(range(1+k,m-k)):
        matrix[k][i]=arr[j]
        j+=1




N, M, R = map(int,sys.stdin.readline().strip().split())

matrix=[]
for i in range(N):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    matrix.append(arr)

for i in range(min(N,M)//2):
    turnMatrix(matrix,N,M,R,i)

for i in matrix:
    for j in i:
        print(j,end=' ')
    print()