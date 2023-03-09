import sys
import copy

N, M= map(int, sys.stdin.readline().strip().split())
dp = [[0] * (M + 1) for _ in range(N + 1)]
loc=[]

for i in range(N):
    loc.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = loc[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]


k=int(sys.stdin.readline())


for i in range(k):
    x_s, y_s, x_e, y_e=(map(int, sys.stdin.readline().strip().split()))
    print(dp[x_e][y_e] - dp[x_e][y_s - 1] - dp[x_s - 1][y_e] + dp[x_s - 1][y_s - 1])