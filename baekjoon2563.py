color_size=0
paper=[[0]*100 for _ in range(100)]
N=int(input())
for i in range(0,N):
    x,y=input().split()
    for a in range(int(x),int(x)+10):
        for b in range(int(y),int(y)+10):
            paper[a][b]=1



color_size=0
for i in paper:
    color_size += i.count(1)

print(color_size)
