from sys import stdin

class vertex():
    def __init__(self,v):
        self.edge=[]
        self.v=v
    
    def insert_edge(self, v, dist):
        self.edge.append([v,dist])

def dfs(v):
    print()


input=stdin.readline

V=int(input())

vertex_set=[]

leaf_node=[]

for i in range(1,V+1):
    vertex_set.append(vertex(i))

for i in range(0,V):
    arr=list(map(int,input().strip().split()))
    arr=arr[1:-1]
    if len(arr)==2:
        leaf_node=[]
    for j in range(1,len(arr),2):
        vertex_set[i].insert_edge(arr[j-1],arr[j])

Max=0
sum=0


print()