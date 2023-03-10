import sys

N=int(sys.stdin.readline())

arr=[0]*N

for i in range(N):
    arr[i]=int(sys.stdin.readline())

top=-1
stack=[0]*N
num=1
Is_NO=False
ans=[]
for i in arr:
    while True:
        if (top==-1 and i==arr[N-1]) or num>N+1:
            Is_NO=True
            break
        if stack[top]!=i:
            top+=1
            ans.append('+')
            stack[top]=num
            num+=1
        else:
            top-=1
            if top==-2:
                break
            ans.append('-')
            break
    if Is_NO==True:
        break
if N==1:
    print('+')
    print('-')
elif Is_NO==False:
    for i in ans:
        print(i)
else:
    print('NO')