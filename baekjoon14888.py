import sys
from itertools import permutations

input=sys.stdin.readline

N=int(input().strip())

arr=list(map(int,input().strip().split()))

math=list(map(int,input().strip().split()))

p=['+']*math[0]
s=['-']*math[1]
m=['*']*math[2]
d=['/']*math[3]

p.extend(s)
p.extend(m)
p.extend(d)

per = list(permutations(p, N-1))
per=set(per)


result=[]
for k in per:
    answer=arr[0]
    for i in range(N-1):
        if k[i]=='+':
            answer += arr[i+1]
        elif k[i]=='-':
            answer -= arr[i+1]
        elif k[i]=='*':
            answer *= arr[i+1]
        elif k[i]=='/':
            if answer<0:
                answer = (-answer)//arr[i+1]
                answer=-answer
            else:
                answer //=arr[i+1]
    result.append(answer)
    
print(max(result))
print(min(result))