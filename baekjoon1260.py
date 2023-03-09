import sys
from collections import deque

class vertex():
    def __init__(self,v_num):
        self.v_num=v_num
        self.edge=[]
        self.flag=False

def dfs(arr, v):
    if v.flag==False:
        print(v.v_num,end=' ')
        v.flag=True
    else:
        return
    for i in v.edge:
        dfs(arr, arr[i])

def bfs(arr, v):
    queue = deque([v.v_num])
    v.flag = True
    while queue:
        ver=queue.popleft()
        print(ver, end=' ')
        for i in arr[ver].edge:
            if arr[i].flag==False:
                queue.append(i)
                arr[i].flag=True

N, M, V=map(int, sys.stdin.readline().split())
arr=[None]
for i in range(1,N+1):
    arr.append(vertex(i))

for _ in range(M):
    v1, v2 = map(int,sys.stdin.readline().split())
    arr[v1].edge.append(v2)
    arr[v2].edge.append(v1)

for i in range(1,N+1):
    arr[i].edge.sort()

dfs(arr,arr[V])
print()
for i in range(1,N+1):
    arr[i].flag=False
bfs(arr,arr[V])