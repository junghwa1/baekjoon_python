word=list(input())
plus_word=[]
T_F=True

middle_char=0

for i in word:
    if i in plus_word:
        continue

    if word.count(i)%2==1 and len(word)%2==0: #특정 문자 홀수 전체 문자 짝수
        T_F=False
        continue
    if word.count(i)%2==1:
        middle=i
        middle_char+=1
    if middle_char>1:
        T_F=False
        continue

    for _ in range(word.count(i)//2):
        plus_word.append(i)

plus_word.sort()


if T_F:
    for s in plus_word: 
        print(s,end='')
    if middle_char>0:
        print(middle,end='')
    for s in plus_word[::-1]: 
        print(s,end='')
else:
    print("I'm Sorry Hansoo")