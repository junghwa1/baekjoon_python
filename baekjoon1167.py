import sys

sys.setrecursionlimit(10**6)



def dfs(v,num):

    for x, y in tree[v]:
        if vertex_dist[x]==-1:
            vertex_dist[x]=y+num
            dfs(x,y+num)


input=sys.stdin.readline


V=int(input())

tree = [[] for _ in range(V+1)]
vertex_dist = [-1] * (V + 1)


for i in range(1,V+1):
    arr=list(map(int,input().strip().split()))

    for j in range(1, len(arr) - 2, 2):
        tree[arr[0]].append([arr[j], arr[j + 1]])


vertex_dist[1]=0
dfs(1,0)
s=vertex_dist.index(max(vertex_dist))
vertex_dist = [-1] * (V + 1)
vertex_dist[s]=0
dfs(s,0)

print(max(vertex_dist))