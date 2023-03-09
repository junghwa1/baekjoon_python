import sys

def loopArr(n,p):
    result=0
    arr=list(str(n))
    for i in arr:
        result+=int(i)**p
    return result

A, P=map(int,sys.stdin.readline().strip().split())

i_list=[]
i_list.append(A)
i=1
while True:
    k=loopArr(i_list[i-1],P)
    
    if k in i_list:
        index=i_list.index(k)
        break
    else:
        i_list.append(k)
        i+=1

print(index)