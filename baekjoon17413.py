import sys

line=list(sys.stdin.readline())
teg=[]
t=False
word=[]
w=True

anwser=[]

for l in line:
    if l=='<' or l=='\n':
        t=True
        w=False
        anwser.append(word[::-1])
        word=[]
    if t==True:
        teg.append(l)

    if w==True and l==' ':
        anwser.append(word[::-1])
        anwser.append(' ')
        word=[]
    
    if w==True and l!= ' ':
        word.append(l)
    
    if l=='>':
        anwser.append(teg)
        teg=[]
        t=False
        w=True
for i in range(len(anwser)):            # 세로 크기
    for j in range(len(anwser[i])):     # 가로 크기
        print(anwser[i][j], end='')
