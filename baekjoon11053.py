from sys import stdin

input=stdin.readline

N=int(input())

arr=list(map(int,input().strip().split()))

dp=[1]*N
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))