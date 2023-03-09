import sys

N=int(sys.stdin.readline())
sum=0

for _ in range(N):
    sum=0
    day=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().strip().split()))
    maxi=arr[day-1]
    for i in arr[::-1]:
        if i > maxi:
            maxi=i
        else:
            sum+=maxi-i
    print(sum)