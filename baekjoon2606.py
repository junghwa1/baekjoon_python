computerNum=int(input())

edgeNum=int(input())

class Graph():
    def __init__(self):
        self.edgeN=[]
        self.edgeN=set(self.edgeN)
        self.vitsit=False
    def edge(self, b):
        self.edgeN.add(b)

vertex=[]
vertex.append(Graph())

for i in range(computerNum):
    vertex.append(Graph())

for i in range(edgeNum):
    a, b =map(int,input().split())
    vertex[a].edge(b)
    vertex[b].edge(a)

sum=[]
sum=set(sum)

def dfs(k):
    if vertex[k].vitsit==False:
        vertex[k].vitsit=True
        sum.add(k)
        for g in vertex[k].edgeN:
             dfs(g)
    else:
        return


dfs(1)
    

sum=list(sum)
print(len(sum)-1)