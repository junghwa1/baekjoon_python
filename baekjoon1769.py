import sys

arr=list(map(int,sys.stdin.readline().strip()))

i=0

while True:
    if len(arr)==1:
        break
    i+=1
    sum=0
    for k in arr:
        sum+=k
    arr=list(map(int,str(sum)))
print(i)
if int(arr[0])%3==0:
    print('YES')
else:
    print("NO")