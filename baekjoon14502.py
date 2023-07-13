from sys import stdin
from collections import deque
import copy

input=stdin.readline

max_num=0

def buildwalls(Lab_s,x,y,cnt):
    if cnt==3:
        bfs(Lab_s)
        return
    
    for i in range(y,N):
        for j in range(M):
            if y==i and j < x:
                continue
            elif Lab_s[i][j]==1 or Lab_s[i][j]==2:
                continue
            Labb=copy.deepcopy(Lab_s)
            Labb[i][j]=1
            buildwalls(Labb,j,i,cnt+1)
            

def bfs(Lab_s):
    queue=deque()
    for i in range(N):
        for j in range(M):
            if Lab_s[i][j]==2:
                queue.append([i,j])
    while queue:
        y,x=queue.popleft()
        if y>=N or y<0:
            continue
        if x>=M or x<0:
            continue

        if Lab_s[y][x]==1 or Lab_s[y][x]==3:
            continue

        if Lab_s[y][x]!=1:
            Lab_s[y][x]=3
            queue.append([y+1,x])
            queue.append([y-1,x])
            queue.append([y,x+1])
            queue.append([y,x-1])

    cnt=0

    for i in range(N):
        for j in range(M):
            if Lab_s[i][j]==0:
                cnt+=1


    global max_num

    if cnt > max_num:
        max_num=cnt


N,M=map(int,input().split())

Lab=[]

for _ in range(N):
    Lab.append(list(map(int, input().strip().split())))


buildwalls(Lab,0,0,0)

print(max_num)