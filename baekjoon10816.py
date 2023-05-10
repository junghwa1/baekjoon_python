from sys import stdin

input=stdin.readline

N=int(input())
cards=list(map(int,input().split()))
cards_set=set(cards)

cards_dic={}

for i in cards_set:
    cards_dic[i]=0

for i in cards:
    cards_dic[i]+=1

M=int(input())

target=list(map(int,input().split()))

for i in target:
    if i in cards_set:
        print(cards_dic[i] , end=' ')
    else:
        print(0, end=' ')