import math
N=input()
arr=[0]*int(N)
for i in range(int(N)):
    x1,y1,r1,x2,y2,r2 = input().split()
    extend=math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2)
    r=int(r1)+int(r2)
    if x1==x2 and y1==y2 and r1!=r2:
        arr[i]=0
    else:
        if x1==x2 and y1==y2 and r1==r2:
            arr[i]=-1
        elif int(r1)+extend==int(r2):
            arr[i]=1
        elif int(r2)+extend==int(r1):
            arr[i]=1
        elif int(r1)+extend<int(r2):
            arr[i]=0
        elif int(r2)+extend<int(r1):
            arr[i]=0
        elif extend==r:
            arr[i]=1
        elif extend>r:
            arr[i]=0
        else:
            arr[i]=2

for i in range(int(N)):
    print(arr[i])