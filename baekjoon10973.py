import sys

N=int(sys.stdin.readline())

num=list(map(int,(sys.stdin.readline().strip().split())))
post=num[N-1]
IsUp=True
end=False
for i in reversed(range(0,N-1)):
    if IsUp==True and num[i]>post:
        num[i+1]=num[i]
        num[i]=post
        break
    elif IsUp==False and num[i]>post:
        sec_max=0
        for j in num[i+1:]:
            if num[i]>j and sec_max<j:
                sec_max=j
        num[num.index(sec_max)]=num[i]
        num[i]=sec_max
        num[i+1:]=sorted(num[i+1:],reverse=True)
        break
    else:
        IsUp=False
    
    post=num[i]
    if i==0:
        end=True
        break

if end==True or N==1:
    print('-1')
else:
    for i in num:
        print(i,end=' ')