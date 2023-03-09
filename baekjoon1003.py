import sys
def fibonacci(n):
    if n == 0 :
        print("0",end='')
        return 0
    elif n == 1:
        print("1",end='')
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

dp_0=[1,0,1,1,2]
dp_1=[0,1,1,2,3]
for i in range(5,41):
    dp_0.append(dp_0[i-1]+dp_0[i-2])
    dp_1.append(dp_1[i-1]+dp_1[i-2])

N=int(sys.stdin.readline())
for _ in range(N):
    k=int(sys.stdin.readline())
    print(dp_0[k],dp_1[k])