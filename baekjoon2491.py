import sys

N = int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().strip().split()))

up=1
down=1
IsUp=True
same=1
maxnum=1
for i in range(1,N):
    if arr[i-1]==arr[i]:
        down+=1
        up+=1
        same+=1
    elif arr[i-1]>arr[i]:
        if IsUp:
            up=1
            down=same+1
        else:
            down+=1
        IsUp=False
        same=1
    else:
        if IsUp:
            up+=1
        else:
            down=1
            up=same+1
        IsUp=True
        same=1
    if maxnum<up:
        maxnum=up
    elif maxnum<down:
        maxnum=down

print(maxnum)