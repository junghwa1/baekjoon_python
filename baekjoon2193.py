import sys

N= int(sys.stdin.readline())

dp=[0]*N
dp[0]=1
if N>1:
    dp[1]=1
for i in range(2,N):
    dp[i]=dp[i-2]+dp[i-1]
if N<=2:
    print(1)
else:
    print(dp[N-1])