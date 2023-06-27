from sys import stdin
import itertools

input=stdin.readline

N,M=map(int,input().split())

arr = list(map(int,input().strip().split()))
com = list(itertools.combinations(arr, 3))

max_num=0

for i in com:
    num=sum(i)
    if num<=M and max_num<num:
        max_num=num

print(max_num)