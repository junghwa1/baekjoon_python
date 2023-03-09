N, num=input().split()
N=int(N)
num=int(num)

arr=[]

    
for i in range(N):
    arr.append(i+1)

print('<', end = '')

i=0

while True:
    i =(i+num-1)%len(arr)   
    print(arr[i],end='')
    del arr[i]
    if len(arr)==0:
        break
    print(', ', end = '')
print('>')