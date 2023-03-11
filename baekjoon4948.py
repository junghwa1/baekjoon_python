import sys
arr=[True]*((123456*2)+1)

arr[0]=False
arr[1]=False

for i in range(2,(123456*2)+1):
    j=1
    if arr[i]==True:
        while True:
            j+=1
            k=i*(j)
            if k >123456*2:
                break
            arr[k]=False

while True:
    N= int(sys.stdin.readline())
    cnt=0
    if N==0:
        break
    for i in arr[N+1:2*N+1]:
        if i==True:
            cnt+=1
    print(cnt)
    