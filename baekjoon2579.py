import sys

N=int(sys.stdin.readline())

stair=[]

for _ in range(N):
    stair.append(int(sys.stdin.readline()))
dp=[0]*N

result=0
if N<=2:
    result=sum(stair)
else:
    dp[0]=stair[0]
    dp[1]=stair[0]+stair[1]
    for i in range(2,N):
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])
    result=dp[N-1]

print(result)