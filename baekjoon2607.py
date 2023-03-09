import sys

N=int(sys.stdin.readline())

cnt=0
c=0


origin=list(sys.stdin.readline().strip())

for _ in range(N-1):
    c=0
    copy_origin=origin[:]
    arr=list(sys.stdin.readline().strip())

    for i in arr:
        if i in copy_origin:
            copy_origin.remove(i)
        else:
            c+=1
    if c<2 and len(copy_origin)<2:
        cnt+=1

    

print(cnt)