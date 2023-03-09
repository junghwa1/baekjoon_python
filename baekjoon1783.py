length, wdith=input().split()
length=int(length)
wdith=int(wdith)

move=0

for _ in range(1):
    if length==1 or wdith==1:
        move=1
        break
    if length==2:
        move=(wdith+1)//2
        if wdith<3:
            move=1
        elif move>=4:
            move=4
    if length>2:
        if wdith<5:
            move=wdith
        elif wdith<7:
            move=4
        elif wdith==7:
            move=5
        else:
            move=wdith-2



print(move)