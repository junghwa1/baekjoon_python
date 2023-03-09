import sys
S_all=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
S_all=set(S_all)
S_n=[]
S_n=set(S_n)
S=[]
S=set(S)

N = int(sys.stdin.readline())
for _ in range(N):
    arr= sys.stdin.readline().split()
    com=arr[0]
    if len(arr)==2:
        num=arr[1] 
        num=int(num)
    if com=='add':
        S.add(num)
    elif com=='remove' and list(S).count(num)==1:
        S.remove(num)
    elif com=='check':
        print(list(S).count(num))
    elif com=='toggle':
        if list(S).count(num)==1:
            S.remove(num)
        else:
            S.add(num)
    elif com=='all':
        S=S_all
    elif com=='empty':
        S=S_n