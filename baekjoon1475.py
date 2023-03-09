import sys
N=list(sys.stdin.readline())
del N[-1]

num=1

setp=['0','1','2','3','4','5','6','7','8','9']
arr=[]
arr.extend(setp) 

for i in N:
    if i in arr:
        arr.remove(i)
    elif i=='6' and '9' in arr:
        arr.remove('9')
    elif i=='9' and '6' in arr:
        arr.remove('6')
    else:
        num+=1
        arr.extend(setp) 
        arr.remove(i)
    

print(num)