import sys
import copy

N = int(sys.stdin.readline())


result=0
dp=[0,1,1,1,1,1,1,1,1,1]
store=[0]*10

for _ in range(1,N):    
    for i in range(0,10):
        if dp[i]!=0:
            if i<=0:
                store[i+1]+=dp[i]
            elif i>=9:
                store[i-1]+=dp[i]
            else:
                store[i+1]+=dp[i]
                store[i-1]+=dp[i]
    dp=copy.deepcopy(store)
    store=[0]*10

print(sum(dp))