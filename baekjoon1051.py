N,M=input().split()
N=int(N)
M=int(M)
box=[]
for _ in range(N):
    box.append(list(input()))

MMin=min(N,M)
size=1
Msize=1

for i in range(0,N-1):
    for j in range(0,M-1):
        LT=box[i][j]
        for k in range(j+1,M):
            if LT==box[i][k]:
                len=k-j
                if i+len<N and box[i+len][j]==LT and box[i+len][k]==LT:
                    size=(len+1)*(len+1)
        if size>Msize:
            Msize=size

print(Msize)