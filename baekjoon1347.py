N=int(input())

EWSN=['S','W','N','E']
S=W=N=E=0
condtion=0
rememo=[]
memo=list(input())
loc_x=[0]
loc_y=[0]

for commend in memo:
    if commend=='F':
        if EWSN[condtion]=='S':
            rememo.append('S')
            S+=1
        elif EWSN[condtion]=='W':
            rememo.append('W')
            W+=1
        elif EWSN[condtion]=='N':
            rememo.append('N')
            N+=1
        else:
            rememo.append('E')
            E+=1

    elif commend=='R':
        condtion+=1
        if condtion>3:
            condtion=0
    else:
        condtion-=1
        if condtion<0:
            condtion=3
x=y=0


for move in rememo:
    if move=='S':
        loc_x.append(loc_x[x])
        loc_y.append(loc_y[y]-1)
        x+=1
        y+=1
    elif move == 'W':
        loc_x.append(loc_x[x]-1)
        loc_y.append(loc_y[y])
        x+=1
        y+=1
    elif move == 'N':
        loc_x.append(loc_x[x])
        loc_y.append(loc_y[y]+1)
        x+=1
        y+=1
    elif move == 'E':
        loc_x.append(loc_x[x]+1)
        loc_y.append(loc_y[y])
        x+=1
        y+=1
    
min_x=min(loc_x)
max_x=max(loc_x)
min_y=min(loc_y)
max_y=max(loc_y)

maze_x=max_x+abs(min_x)
maze_y=max_y+abs(min_y)

temp_x=abs(min_x)
temp_y=abs(min_y)


maze=[['#']*(maze_x+1) for _ in range(maze_y+1)]


for move_x, move_y in zip(loc_x,loc_y):
    maze[temp_y+move_y][temp_x+move_x]='.'

for i in range(maze_y+1):
    for j in range(maze_x+1):
        print(maze[maze_y-i][j], end='')
    print()
