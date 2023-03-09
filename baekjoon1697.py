import sys
from collections import deque

class vertex():
    def __init__(self,v_num):
        self.v_num=v_num
        self.flag=False
        if self.v_num==100000:
            self.edge=[99999]
        elif self.v_num>1 and self.v_num<=50000:
            self.edge=[v_num-1,v_num+1,2*v_num]
        elif self.v_num>=50001:
            self.edge=[v_num-1,v_num+1]
        elif self.v_num==1:
            self.edge=[0,2]
        elif self.v_num==0:
            self.edge=[1]


def bfs(arr, v,k):
    queue=deque([v.v_num])
    v.flag=True
    cnt=0
    last=v.v_num
    ver=v.v_num
    while queue:
        ver=queue.popleft()
        
        for i in arr[ver].edge:
            if arr[i].flag==False:
                queue.append(i)
                arr[i].flag=True
                if k==i:
                    return cnt+1
        if last==ver:
            cnt+=1
            last=queue.pop()
            queue.append(last)




N, K = map(int, sys.stdin.readline().split())
arr=[]
for i in range(100001):
    arr.append(vertex(i))

if N>K:
    print(N-K)
elif N==K:
    print(0)
elif N+1==K or N*2==K:
    print(1)
else:
    print(bfs(arr,arr[N],K))
