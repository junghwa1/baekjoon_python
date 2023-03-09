import sys

def prime_list(n):
    num = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if num[i] == True:
            for j in range(i+i, n, i):
                num[j] = False


    return [i for i in range(2, n) if num[i] == True]

M, N =map(int,sys.stdin.readline().split())

for i in prime_list(N+1):
    if M<=i and i <=N:
        print(i) 
    