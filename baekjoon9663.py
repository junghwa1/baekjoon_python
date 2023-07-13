from sys import stdin

input=stdin.readline

def N_Q(r):
    
    
    global result
    if r==N:
        result+=1
        return
    
    for k in range(N):    
        row[r]=k
        T_F=True
        for i in range(r):
            if i==r or row[i]==row[r] or abs(row[i]-row)==abs(i-r):
                T_F=False
            else:
                T_F=True
            if T_F==True:
                N_Q(r+1)
    


N=int(input())
row=[0]*N

result=0
N_Q(0)

print(result)