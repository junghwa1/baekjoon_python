board=[[0]*6 for _ in range(6)]
ABC=['A','B','C','D','E','F']
ex_move=[[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
move=[]
answer=True
post_chess = input()
post_chess=list(post_chess)
first_chess=post_chess
board[ABC.index(post_chess[0])][int(post_chess[1])-1]=1
for i in range(0,35):
    chess=input()
    chess=list(chess)
    if board[ABC.index(chess[0])][int(chess[1])-1]==1:
        answer=False
    board[ABC.index(chess[0])][int(chess[1])-1]=1
    x=ABC.index(chess[0])-ABC.index(post_chess[0])
    y=int(chess[1])-int(post_chess[1])
    move=[x,y]
    if move not in ex_move:
        answer=False
    post_chess=chess

x=ABC.index(first_chess[0])-ABC.index(post_chess[0])
y=int(first_chess[1])-int(post_chess[1])
move=[x,y]
if move not in ex_move:
    answer=False

if answer:
    print("Valid")
else:
    print("Invalid")