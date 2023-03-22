import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
arr=list(map(int, input().split()))

queue=deque()

for i in range(N):
    queue.append((arr[i],i+1))

while queue:
    i,index=queue.popleft()
    
    if not queue:
        print(index)
        break
    print(index,end=' ')
    if i>0:
        queue.rotate(-(i-1))
    else:
        queue.rotate(-i)