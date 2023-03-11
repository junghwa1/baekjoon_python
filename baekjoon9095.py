import sys

N= int(sys.stdin.readline())

dp=[1,2,4]
for i in range(3,11):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for i in range(N):
    k= int(sys.stdin.readline())
    print(dp[k-1])