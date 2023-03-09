import sys

N=int(sys.stdin.readline())
dp=[0,0,1,1,2]

for i in range(5,N+1):
    a,b,c=0,0,0
    if i%2==0:
        a=i//2
    else:
        a=i-1
    if i%3==0:
        b=i//3
    else:
        b=i-1
    c=i-1
    
    k=min(dp[a],dp[b],dp[c])
    dp.append(k+1)


print(dp[N])