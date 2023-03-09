import sys

def check(ox):
    cnt=0
    a=0
    b=0
    for i in ox:
        if i.count(1)==5:
            cnt+=1
        
    
    for i in range(5):
        if ox[i][i]==1:
            a+=1
        if ox[4-i][i]==1:
            b+=1
    if a==5:
        cnt+=1
    if b==5:
        cnt+=1
    
    for i in range(5):
        a=0
        for j in range(5):
            if ox[j][i]==1:
                a+=1
        if a==5:
            cnt+=1
    return cnt


bingo=[]
ox=[[0]*5 for _ in range(5)]
ask=[]

for i in range(5):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    bingo.append(arr)

for i in range(5):
    arr=list(map(int,sys.stdin.readline().strip().split()))
    ask.append(arr)
flag=0
c=0
for a in range(5):
    for b in range(5):
        c+=1
        for i in range(5):
            for j in range(5):
                if ask[a][b]==bingo[i][j]:
                    ox[i][j]=1
                    if check(ox)>=3:
                        flag=1
            if flag==1:
                break
        if flag==1:
            break
    if flag==1:
        break
print(c)