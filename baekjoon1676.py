import sys

N=int(sys.stdin.readline())

mul=1
for i in range(1,N+1):
    mul*=i

sum=0
while True:
    if mul%10==0:
        sum+=1
    else:
        break
    mul=mul//10

print(sum)