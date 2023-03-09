word=input()

answer=[]
new_word=''
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        a=word[:i]
        new_word=new_word+a[::-1]
        a=word[i:j]
        new_word=new_word+a[::-1]
        a=word[j:]
        new_word=new_word+a[::-1]
        answer.append(new_word)
        new_word=''
answer.sort()
print(answer[0])