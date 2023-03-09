import sys
from collections import deque

N=int(sys.stdin.readline())
Is_error=False
for _ in range(N):
    commend=list(sys.stdin.readline().strip())
    a=int(sys.stdin.readline())
    p=sys.stdin.readline().rstrip()[1:-1].split(',')
    queue=deque(p)
    R_num=0

    for i in commend: 
        if i=='D':
            if not queue or a==0:
                Is_error=True
                print('error')
                break
            if R_num%2==0:
                queue.popleft()
            else:
                queue.pop()
        if i=='R':
            R_num+=1

    if Is_error==False:
        if R_num%2==0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
    Is_error=False