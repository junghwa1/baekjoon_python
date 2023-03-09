A,B=input().split()

set_A=[]
set_B=[]
strA=input()
set_A=set(strA.split())
strB=input()
set_B=set(strB.split())
count=0
A_Bc=set_A-set_B
B_Ac=set_B-set_A
count=len(A_Bc)
count+=len(B_Ac)
print(count)