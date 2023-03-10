import sys

N=int(sys.stdin.readline())

arr=[]
result=0

for i in range(N):
    a=int(sys.stdin.readline())
    arr.append(a)


dp=[0]*N
dp[0]=arr[0]
if N>1:
    dp[1]=arr[0]+arr[1]

for i in range(2,N):
    dp[i]=max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])

print(dp[N-1])
