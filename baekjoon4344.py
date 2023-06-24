from sys import stdin

input=stdin.readline

C=int(input())

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

for _ in range(C):
    arr=list(map(int,input().strip().split()))
    avg=sum(arr[1:])/arr[0]
    num=0
    for j in arr[1:]:
        if avg<j:
            num+=1

    result = num/arr[0]*100
    print(f'{roundTraditional(result, 3):.3f}%' )
    