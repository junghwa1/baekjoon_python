from sys import stdin

input=stdin.readline

N, M = map(int,input().split())

hear=[]
see=[]

for i in range(N):
    hear.append(input().strip())

for i in range(M):
    see.append(input().strip())

hear=set(hear)
see=set(see)

hear_see=hear&see

hear_see=list(hear_see)
hear_see.sort()

print(len(hear_see))
for i in hear_see:
    print(i)