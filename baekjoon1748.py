import sys

N=sys.stdin.readline().strip()

arr=[]
arr=list(N)

N=int(N)
result=0
l=len(arr)

result+=(N-10**(l-1)+1)*l
for i in range(1,l):
    result+=9*(10**(i-1))*i
print(result)