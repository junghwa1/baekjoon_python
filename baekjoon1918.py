from sys import stdin

input=stdin.readline
stack=[]

def trans(word):
    if word=='+' or word=='-':
        return 1
    elif word=='*' or word=='/':
        return 2
    else:
        return 0

arr=input().strip()


for i in arr:
    if i.isalpha():
        print(i ,end= '')
    elif i=='(':
        stack.append(i)
    elif i==')':
        while stack and stack[-1]!='(':
            print(stack.pop() ,end= '')
        stack.pop()
    elif trans(i):
        while stack and trans(stack[-1])>=trans(i):
            print(stack.pop() ,end= '')
        stack.append(i)
while stack:
    print(stack.pop() ,end= '')