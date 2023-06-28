from sys import stdin

input=stdin.readline

N=int(input())

arr=[]

for _ in range(N):
    arr.append(list(map(int,input().split())))

cnt=0

for i in range(1,N):
    while cnt<=i:
        if cnt==0:
            arr[i][cnt]+=arr[i-1][cnt]
        elif cnt==i:
            arr[i][cnt]+=arr[i-1][cnt-1]
        else:
            arr[i][cnt]+=max(arr[i-1][cnt-1],arr[i-1][cnt])
        cnt+=1
    cnt=0


print(max(arr[N-1]))