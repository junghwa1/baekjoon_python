from sys import stdin

input=stdin.readline

N, K =map(int, input().split())
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1,N+1):
    W, V =map(int, input().split())
    for j in range(1,K+1):
        if j < W:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(V + bag[i - 1][j - W], bag[i - 1][j])
print(bag[N][K])