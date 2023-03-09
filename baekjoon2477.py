import sys

N = int(sys.stdin.readline().strip())
EWSN=[0,0,0,0]
count=[]
for _ in range(6):
    x,y=map(int, sys.stdin.readline().strip().split())
    EWSN[x-1]+=1
    count.append([x,y])
    

a=0
b=1
c=2
d=3
k=0
while True:
    if count[a][0]==count[c][0] and count[b][0]==count[d][0]:
        k=count[b][1]*count[c][1]
        break
    
    a=(a+1)%6
    b=(b+1)%6
    c=(c+1)%6
    d=(d+1)%6

m=1
for i in range(4):
    if EWSN[i]==1:
        for j in range(6):
            if count[j][0]==i+1:
                m*=count[j][1]

print((m-k)*N)