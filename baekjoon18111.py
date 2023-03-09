import sys

N, M, B =map(int,sys.stdin.readline().split())
land=[]

for _ in range(N):
    land.extend(list(map(int,sys.stdin.readline().split())))

min_sec=sys.maxsize
max_floor=0
for floor in range(0,257):
    fill,dig=0,0
    for i in land:
        dif=i-floor
        if dif>=0:
            dig+=dif
        else:
            fill+=-dif
    if fill>dig+B:
        continue
    sec=dig*2+fill

    if min_sec>=sec:
        min_sec=sec
        max_floor=floor

print(min_sec,max_floor)