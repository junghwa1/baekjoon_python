from sys import stdin
import copy
input=stdin.readline

N=int(input())

arr=list(map(int,input().strip().split()))

sorted_arr=set(arr)
sorted_arr=list(sorted_arr)
sorted_arr.sort()

dict_arr={}
cnt=0
for i in sorted_arr:
    dict_arr[i]=cnt
    cnt+=1

for i in arr:
    print(dict_arr[i],end=' ')