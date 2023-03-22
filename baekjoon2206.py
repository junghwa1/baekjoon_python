import sys
from collections import deque

input=sys.stdin.readline

N, M=map(int,input().split())
maze=[]
maze_cnt=[[[0]*2 for _ in range(M)] for _ in range(N)]
maze_cnt[0][0][0]=1

for i in range(N):
    maze.append(list(map(int,input().strip())))

vec_x = [0, 0, 1, -1]
vec_y = [1, -1, 0, 0]

def bfs(maze, maze_cnt,N,M):
    queue=deque()
    queue.append((0,0,0))
    while queue:
        x,y,c=queue.popleft()
        if x==N-1 and y==M-1:
            return maze_cnt[x][y][c]
        for i in range(4):
            nx = x + vec_x[i]
            ny = y + vec_y[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 1 and c == 0 :
                maze_cnt[nx][ny][1] = maze_cnt[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif maze[nx][ny] == 0 and maze_cnt[nx][ny][c] == 0:
                maze_cnt[nx][ny][c] = maze_cnt[x][y][c] + 1
                queue.append((nx, ny, c))
 
    return -1      

result=bfs(maze, maze_cnt,N,M)

if N==1 and M==1:
    print(1)
else:
    print(result)