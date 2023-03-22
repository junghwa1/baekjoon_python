from sys import stdin
import heapq

INF=int(1e9)    


V, E=map(int, stdin.readline().strip().split())

start=int(stdin.readline())

graph=[[] for _ in range(V+1)]
distance=[INF]*(V+1)

for _ in range(E):
    s_v, e_v, dis= map(int, stdin.readline().split())
    graph[s_v].append((e_v,dis))

def dajkstra(graph, start,distance):
    queue=[]
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        dis, current=heapq.heappop(queue)
        if dis>distance[current]:
            continue
        for e_v,e_dis in graph[current]:
            if distance[e_v]>dis+e_dis:
                distance[e_v]=dis+e_dis
                heapq.heappush(queue,(dis+e_dis,e_v))
dajkstra(graph,start,distance)
for i in distance[1:]:
    if i==INF:
        print('INF')
    else:
        print(i)
