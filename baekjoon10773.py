import sys

N=int(sys.stdin.readline())

numArr=[]

for i in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        del numArr[len(numArr)-1]
    else:
        numArr.append(num)

print(sum(numArr))
