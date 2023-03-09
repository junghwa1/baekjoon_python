import sys
from itertools import permutations

N=int(sys.stdin.readline())
ask_list=[]

items = [1,2,3,4,5,6,7,8,9]
i_list = list(permutations(items,3))

for i in range(N):
    ask=list(map(int,sys.stdin.readline().strip().split()))
    ask_list.append(ask)

cnt=0
IsTure=False
for num in i_list:
    IsTrue=True
    for ask in ask_list:
        s=0
        b=0
        ask_num=list(map(int,str(ask[0])))
        for i in range(3):
            if ask_num[i]==num[i]:
                s+=1
            elif num[i] in ask_num:
                b+=1
        if ask[1]!=s or ask[2]!=b:
            IsTrue=False
    if IsTrue==True:
        cnt+=1

print(cnt)