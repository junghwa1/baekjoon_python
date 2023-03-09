import sys

N =int(sys.stdin.readline())
student=[0]*101
img=[]
M =int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))
for i in arr:
    if i in img:
        student[i]+=1
        continue
    if len(img)==N:
        b=img[0]
        for a in img[1:]:
            if student[a]<student[b]:
                b=a
        img.remove(b)
        student[b]=0
    if i not in img:
        img.append(i)
        student[i]+=1
img.sort()
for i in img:
    print(i,end=' ')