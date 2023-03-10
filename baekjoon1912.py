import sys

N = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))

post_sum=0
max_sum=arr[0]
sum=0
for i in arr:
    sum+=i
    max_sum=max(max_sum,sum,sum-post_sum)
    post_sum=min(sum,post_sum)
    
print(max_sum)
