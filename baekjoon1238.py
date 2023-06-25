from sys import stdin
import heapq

def dijkstra(graph,v):
    queue=[]
    dist[v]=0
    heapq.heappush(queue,(v,0))
    while queue:
        current,d=heapq.heappop(queue)
        if dist[current]<d:
            continue
        for i in graph[current]:
            cost=d+i[1]

            if cost < dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(queue,(i[0],cost))

INF=int(1e8)
input=stdin.readline

N,M,X =map(int,input().split())

dist=[INF]*(N+1)

graph=[[] for _ in range(N+1)]
reversed_graph=[[] for _ in range(N+1)]

for i in range(1,M+1):
    start, end, time = map(int, input().split())
    graph[start].append([end,time])

result=[]
dijkstra(graph,X)
result.append(dist)
dist=[INF]*(N+1)

for i in range(1,N+1):
    end=i
    for start, time in graph[i]:
        reversed_graph[start].append([end,time])

dijkstra(reversed_graph,X)
result.append(dist)
dist=[INF]*(N+1)

sum_num=[]

for i in range(1,N+1):
    sum_num.append(result[0][i]+result[1][i])

print(max(sum_num))