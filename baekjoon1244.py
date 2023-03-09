N=int(input())


switch=input().split()
switch=list(map(int, switch))

def change_button(num):
    if switch[num-1]==1:
        switch[num-1]=0
    else:
        switch[num-1]=1

stu_num=int(input())

for _ in range(stu_num):
    stu_sex, switch_num=input().split()
    stu_sex=int(stu_sex)
    switch_num=int(switch_num)
    if stu_sex==1:
        for i in range(1,N+1):
            if i%switch_num==0:
                change_button(i)
    elif stu_sex==2:
        range_num=1
        while(True):
            if range_num==1:
                change_button(switch_num)
            if switch_num-range_num-1>=0 and switch_num+range_num-1<=N-1:
                if switch[switch_num-range_num-1] == switch[switch_num+range_num-1]:
                    change_button(switch_num-range_num)
                    change_button(switch_num+range_num)
                else:
                    break
            else:
                break
            range_num+=1

for i in range(1,N+1):
    print(switch[i-1] , end=' ')
    if i%20==0:
        print('')
