import sys

N=int(sys.stdin.readline())

dp_R=[0]*N
dp_G=[0]*N
dp_B=[0]*N
dp_R[0], dp_G[0], dp_B[0] = map(int, sys.stdin.readline().split())
for i in range(1,N):
    R, G, B = map(int, sys.stdin.readline().split())
    dp_R[i]=min(dp_G[i-1],dp_B[i-1])+R
    dp_G[i]=min(dp_R[i-1],dp_B[i-1])+G
    dp_B[i]=min(dp_R[i-1],dp_G[i-1])+B

print(min(dp_R[N-1],dp_G[N-1],dp_B[N-1]))