import sys

loop=int(sys.stdin.readline())

queue=[]

want=[]

def dequeue():
    del queue[0]
    i=want[0]
    del want[0]
    return i

def back():
    k=queue[0]
    del queue[0]
    queue.append(k)
    l=want[0]
    del want[0]
    want.append(l)

def printPaper():
    sum=1
    while(len(queue)):
        if len(queue)==1:
            return sum
        if max(queue)!=queue[0]:
            back()
        else:
            if dequeue()==1:
                return sum
            sum+=1
        if len(queue)==1:
            break
    return sum  
            



for _ in range(loop):
    N, M =map(int,sys.stdin.readline().split())

    queue=list(map(int,sys.stdin.readline().split()))
    want=[0]*len(queue)
    want[M]=1

    
    print(printPaper())





