from sys import stdin

input=stdin.readline
cant_use=[0]*10
num=input().strip()
a=list(map(int,num))
N=int(input())
if N!=0:
    k=list(map(int,input().split()))
    for i in k:
        cant_use[i]=1
num=int(num)
T_F=True
Min=1000001
for i in range(0,1000001):
    target=list(map(int,str(i)))
    for j in target:
        if cant_use[j]==1:
            T_F=False
    if T_F==False:
        T_F=True
        continue
    result=abs(num-i)+len(target)
    if Min>result:
        Min=result

if num==100:
    Min=0

sub=abs(num-100)

if Min >sub:
    Min=sub
print(Min)