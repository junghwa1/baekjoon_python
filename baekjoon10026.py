import sys

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs_RG(arr,visited,dx,dy,x,y,color):
    if x<0 or y<0 or x>=N or y>=N:
        return
    if visited[x][y]==1:
        return
    if color=='B':
        if arr[x][y]!='B':
            return
    else:
        if arr[x][y]!='G' and arr[x][y]!='R':
            return
    visited[x][y]=1
    for i in range(4):
        dfs_RG(arr,visited,dx,dy,x+dx[i],y+dy[i],color)

def dfs(arr,visited,dx,dy,x,y,color):
    if x<0 or y<0 or x>=N or y>=N:
        return
    if visited[x][y]==1 or arr[x][y]!=color:
        return
    visited[x][y]=1
    for i in range(4):
        dfs(arr,visited,dx,dy,x+dx[i],y+dy[i],color)


N=int(sys.stdin.readline())

arr=[[]]*N
visited=[[0]*N for _ in range(N)]
for i in range(N):
    arr[i]=list(sys.stdin.readline().strip())

cnt=0

for i in range(N):
    for j in range(N):
        if visited[i][j]==1:
            continue
        dfs(arr,visited,dx,dy,i,j,arr[i][j])
        cnt+=1

print(cnt,end=' ')

visited=[[0]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==1:
            continue
        dfs_RG(arr,visited,dx,dy,i,j,arr[i][j])
        cnt+=1


print(cnt)