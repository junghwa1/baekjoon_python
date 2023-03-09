import sys

p,m=map(int,sys.stdin.readline().strip().split())
IsIn=False
bang=[]
player=[]
for _ in range(p):
    level, name = sys.stdin.readline().strip().split()
    level=int(level)
    player=[level,name]
    if len(bang)==0:
        bang.append([player])
    else:
        for i in bang:
            target_level=i[0][0]
            if level <= target_level + 10 and target_level - 10 <= level and len(i)<m:
                i.append(player)
                IsIn=True
                
                break

        if IsIn==False:
            bang.append([player])
        IsIn=False

for i in bang:
    if len(i)<m:
        i.sort(key=lambda x:x[1])
        print("Waiting!")
        for j in i:
            print(j[0],j[1])
    if len(i)==m:
                    print("Started!")
                    i.sort(key=lambda x:x[1])
                    for j in i:
                        print(j[0],j[1])