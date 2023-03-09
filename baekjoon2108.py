import sys

N = int(sys.stdin.readline())
arr=[]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
summ=int(sum(arr))
if summ>=0:
    print(int(sum(arr)/N+0.5))
else:
    print(int(sum(arr)/N-0.5))
arr.sort()
print(arr[N//2])

arr.sort()
cnt = {}
for i in range(N):
    if arr[i] not in cnt.keys():
        cnt[arr[i]] = 1
    else:
        cnt[arr[i]] += 1
cnt = sorted(cnt.items(), key = lambda x:(-x[1], x[0]))
for i in range(len(cnt)):
    cnt[i] = list(cnt[i])
if len(cnt) == 1 or cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
else:
    print(cnt[1][0])

print(max(arr)-min(arr))