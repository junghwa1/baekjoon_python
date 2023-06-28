from sys import stdin

input=stdin.readline

A ,B, K=map(int, input().split())

result=1

def pow(C,n):
    if n==1:
        return C%K
    result=pow(A,n//2)

    if n%2==0:
        return result*result%K
    else:
        return result*result*C%K



print(pow(A,B))