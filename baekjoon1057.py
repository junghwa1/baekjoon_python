import math
n,a,b=input().split()
count=1
n=int(n)
a=int(a)
b=int(b)
for _ in range(n):
    arr=[a,b]
    m=max(arr)
    if abs(b-a)==1 and m%2==0:
        break
    count+=1
    if a%2==0:
        a=a//2
    else:
        a=a//2+1
    
    if b%2==0:
        b=b//2
    else:
        b=b//2+1

print(count)