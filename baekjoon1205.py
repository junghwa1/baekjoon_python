N, score, P=input().split()
N=int(N)
score=int(score)
P=int(P)
if N!=0:
    M=input().split()
    M=list(map(int, M))
    M.append(score)
    M.sort(reverse=True)
    rank=M.index(score)+1
    
    if P<rank or(P==N and M[-1]==M[-2]):
        print('-1')
    else:
        print(rank)    
else:
    print('1')

