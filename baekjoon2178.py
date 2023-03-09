import sys
from collections import deque

def bfs(maze,N,M):

    queue_x=deque()
    queue_y=deque()
    queue_x.append(0)
    queue_y.append(0)
    
    while queue_x or queue_y:
        x=queue_x.popleft()
        y=queue_y.popleft()
        if maze[x][y]!=0 and x!=0 and not(x-1==0 and y==0):
            if maze[x-1][y]>maze[x][y]+1 or maze[x-1][y]==1:
                maze[x-1][y]=maze[x][y]+1
                queue_x.append(x-1)
                queue_y.append(y)
        if maze[x][y]!=0 and y!=0 and not(x==0 and y-1==0):
            if maze[x][y-1]>maze[x][y]+1 or maze[x][y-1]==1:
                maze[x][y-1]=maze[x][y]+1
                queue_x.append(x)
                queue_y.append(y-1)
        if maze[x][y]!=0 and x!=N-1 and not(x+1==0 and y==0):
            if maze[x+1][y]>maze[x][y]+1 or maze[x+1][y]==1:
                maze[x+1][y]=maze[x][y]+1
                queue_x.append(x+1)
                queue_y.append(y)
        if maze[x][y]!=0 and y!=M-1 and not(x==0 and y+1==0):
            if maze[x][y+1]>maze[x][y]+1 or maze[x][y+1]==1:
                maze[x][y+1]=maze[x][y]+1            
                queue_x.append(x)
                queue_y.append(y+1)


N,M = map(int, sys.stdin.readline().split())

maze=[]

for _ in range(N):
    maze.append(list(map(int,sys.stdin.readline().strip())))

bfs(maze,N,M)

print(maze[N-1][M-1])

