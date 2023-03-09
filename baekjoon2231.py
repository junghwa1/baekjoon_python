num=input()
size=len(num)
result=0
sum=0
d=1
while True:
    sum=d
    for j in str(d):
        sum+=int(j)
    if sum==int(num):
        result=d
        break
    d+=1
    if d ==1000000:
        break
print(result)