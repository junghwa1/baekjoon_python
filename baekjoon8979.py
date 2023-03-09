import sys

N, K =map(int, sys.stdin.readline().strip().split())

contry=[]

for _ in range(N):
    contry.append(list(map(int, sys.stdin.readline().strip().split())))

g=0

#나라번호 / 금 / 은 / 동
contry.sort(key=lambda x:x[1])
i=0
while True:
    if contry[i][0]==K:
        target=contry[i]
        g=i
        break
    i+=1
rank=1
for j in range(0,N):
    if contry[j][1]>target[1]:
        rank+=1
    elif contry[j][1]==target[1] and contry[j][2]>target[2]:
        rank+=1
    elif contry[j][1]==target[1] and contry[j][2]==target[2] and contry[j][3]>target[3]:
        rank+=1

print(rank)