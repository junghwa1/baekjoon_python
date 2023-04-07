import sys
from collections import deque

dx=[0,1,0,-1,0,0]
dy=[1,0,-1,0,0,0]
dz=[0,0,0,0,1,-1]

def bfs(M,N,H):
    queue=deque()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y]==1:
                    queue.append((x,y,z,0))
    cnt=0       
    while queue:
        i,j,k,c=queue.popleft()
        for w in range(6):
            if 0<=i+dx[w] and i+dx[w] < N and 0<=j+dy[w] and j+dy[w]<M and 0<= k+dz[w] and k+dz[w]<H:
                if box[k+dz[w]][i+dx[w]][j+dy[w]]==0:
                    box[k+dz[w]][i+dx[w]][j+dy[w]]=1
                    queue.append((i+dx[w],j+dy[w],k+dz[w],c+1))
            if cnt<c:
                cnt=c
    return cnt

input = sys.stdin.readline

M, N, H = map(int ,input().split())

box=[]


for i in range(H):
    box.append([])
    for _ in range(N):
        box[i].append(list(map(int, input().split())))

answer=bfs(M,N,H)
for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y]==0:
                    answer=-1
                    break
print(answer)