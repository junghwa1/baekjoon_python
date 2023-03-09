import sys

arr=list(sys.stdin.readline())
del arr[-1]
top=len(arr)-1
a=0
T_F=True
top=-1
result=0
stack=[0]*len(arr)
for i in arr:
    a+=1
    result=0
    top+=1
    stack[top]=i
    if top>=1:
        if stack[top]==')':
            while True:
                top-=1
                if top ==-2:
                    T_F=False
                    break
                if stack[top]=='(':
                    if result==0:
                        result=1
                    break
                if type(stack[top])==int:
                    result+=stack[top]
                else:
                    T_F=False
            if T_F==False:
                break
            stack[top]=result*2
        elif stack[top]==']':
            while True:
                top-=1
                if top ==-2:
                    T_F=False
                    break
                if stack[top]=='[':
                    if result==0:
                        result=1
                    break
                if type(stack[top])==int:
                    result+=stack[top]
                else:
                    T_F=False
                
            if T_F==False:
                break
            stack[top]=result*3
                
anwser=0

if T_F==False or len(arr)<=1:
    print('0')
else:
    for i in range(0,top+1):
        if type(stack[i])==int:
            anwser+=stack[i]
        else:
            anwser=0
            break
    print(anwser)