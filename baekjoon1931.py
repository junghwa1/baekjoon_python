import sys

N=int(sys.stdin.readline())

all_time=[]

for _ in range(N):
    start_time, end_time= map(int, sys.stdin.readline().split())
    all_time.append([start_time,end_time])

all_time.sort(key=lambda x:(x[1],x[0]))

last=all_time[0]
cnt=1

for i in all_time[1:]:
    if last[1]<=i[0]:
        last=i
        cnt+=1
        
print(cnt)