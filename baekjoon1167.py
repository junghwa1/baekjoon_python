import sys
sys.setrecursionlimit(10**6)

def dfs(v,num):
    for x, y in tree[v]:
        if vertex_dist[x]==-1:      #방문하지 않은 정점이라면 가중치를 더해가며 저장
            vertex_dist[x]=y+num
            dfs(x,y+num)

input=sys.stdin.readline

V=int(input())

tree = [[] for _ in range(V+1)]
vertex_dist = [-1] * (V + 1)

for i in range(1,V+1):
    arr=list(map(int,input().strip().split()))
    for j in range(1, len(arr) - 2, 2):
        tree[arr[0]].append([arr[j], arr[j + 1]])   #연결된 정점과 가중치만 저장


vertex_dist[1]=0
dfs(1,0)
y=vertex_dist.index(max(vertex_dist))   #가장 거리가 먼 정점을 찾고
vertex_dist = [-1] * (V + 1)    #초기화
vertex_dist[y]=0
dfs(y,0)        #y를 통해 트리의 지름 구하기

print(max(vertex_dist))