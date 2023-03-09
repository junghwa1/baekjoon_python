import sys
import math
N= int(sys.stdin.readline())
n=N
r=0
sum=0
while n>=r:
    sum+=math.comb(n,r)
    r+=1
    n-=1

print(sum%10007)
