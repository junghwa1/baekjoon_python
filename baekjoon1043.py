from sys import stdin
from collections import deque

def bfs(a):
    visited[a]=1
    queue=deque()
    queue.append(a)
    
    while queue:
        k=queue.popleft()
        visited[k]=1
        arr=graph[k]
        for i in arr:
            if visited[i]==0:
                queue.append(i)

graph={}
visited=[0]*51
input=stdin.readline

N, M =map(int,input().split())

k=list(map(int,input().strip().split()))

if k[0]!=0:
    for i in k[1:]:
        graph[i]=k[1:]
p=[0]*M
for i in range(M):
    p[i]=list(map(int,input().strip().split()))
    for j in p[i][1:]:
        graph[j]=p[i][1:]

for i in range(M):
    for j in p[i][1:]:
        a=graph[j]
        a=set(a)
        a=a|set(p[i][1:])
        graph[j]=list(a)


for i in k[1:]:
    bfs(i)

cnt=0

T_F=True

for i in range(M):
    for j in p[i][1:]:
        if visited[j]==1:
            T_F=False
    if T_F==True:
        cnt+=1
    T_F=True


print(cnt)