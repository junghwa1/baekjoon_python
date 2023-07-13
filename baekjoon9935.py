from sys import stdin

input=stdin.readline

arr=list(input().strip())
boom=list(input().strip())
boomlen=len(boom)

stack=[]

for i in arr:
    stack.append(i)
    stacklen=len(stack)
    if stacklen >=boomlen:
        if stack[stacklen-boomlen:]==boom:
            for j in range(boomlen):
                stack.pop()
if stack:
    for i in stack:
        print(i,end='')
else:
    print('FRULA')