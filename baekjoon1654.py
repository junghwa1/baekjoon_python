import sys

K ,N=map(int, sys.stdin.readline().split())

H_line=[]

for i in range(K):
    H_line.append(int(sys.stdin.readline()))


left,right=1,max(H_line)
result=0
a=0
while True:
    cnt=0
    mid=(left+right)//2
    for wood in H_line:
        cnt+=wood//mid
    if cnt>=N:
        result=mid
        left=mid+1
        if mid>a:
            a=mid
        else:
            break

    else:
        right=mid-1

if result==0:
    result=max(H_line)


print(result)