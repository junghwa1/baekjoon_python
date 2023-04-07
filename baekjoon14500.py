import sys
from collections import deque

def bfs(paper,x,y):
    cnt=0
    max_res=0
    queue = deque()
    queue.append((x,y,paper[x][y],cnt))
    while queue:
        i, j , k, c= queue.popleft()
        if k==12:
            continue
        if c==3:
            if max_res < k:
                max_res=k
            continue
        if i+1<M:
            queue.append((i+1,j,k+paper[i+1][j],c+1))
        if i-1>=0:
            queue.append((i-1,j,k+paper[i-1][j],c+1))
        if j+1<M:
            queue.append((i,j+1,k+paper[i][j+1],c+1))
        if j-1>=0:
            queue.append((i,j-1,k+paper[i][j-1],c+1))

    return max_res

input=sys.stdin.readline

N, M =map(int,input().strip().split())
paper=[]
max_num=0
for _ in range(N):
    paper.append(list(map(int,input().rstrip().split())))

for i in range(N):
    for j in range(M):
        num=bfs(paper,i,j)
        if max_num<num:
            max_num=num
print(max_num)
