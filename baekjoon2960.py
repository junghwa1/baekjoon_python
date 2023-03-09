import sys

N,k=map(int,sys.stdin.readline().strip().split())

arr=[1]*N
arr[0]=0
a=2
mul=2
count=0
i=1
while True:
    if count==N-1:
        break 
    if a>len(arr):
        mul=arr.index(1)+1
        a=mul
        i=1
        continue
    if arr[a-1]==1:
        arr[a-1]=0
        count+=1
    if count==k:
        break
    i+=1
    a=mul*i
print(a)