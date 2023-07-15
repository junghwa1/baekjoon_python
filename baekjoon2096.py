from sys import stdin

input=stdin.readline

temp=[]

N=int(input())
maxmin=list(map(int,input().strip().split()))*2
for i in range(N-1):
    temp=list(map(int,input().strip().split()))*2

    max0=max(maxmin[0],maxmin[1])+temp[0]
    max1=max(maxmin[0],maxmin[1],maxmin[2])+temp[1]
    max2=max(maxmin[1],maxmin[2])+temp[2]
    max3=min(maxmin[3],maxmin[4])+temp[3]
    max4=min(maxmin[3],maxmin[4],maxmin[5])+temp[4]
    max5=min(maxmin[4],maxmin[5])+temp[5]
    maxmin[0]=max0
    maxmin[1]=max1
    maxmin[2]=max2
    maxmin[3]=max3
    maxmin[4]=max4
    maxmin[5]=max5




print(max(maxmin[:3]),min(maxmin[3:]))