st=input()
U=False
C1=False
P=False
C2=False

if not U:
    if st.find('U')+1:
        index=st.find('U')
        st=st[index+1:]
        U=True
if not C1:
    if st.find('C')+1:
        index=st.find('C')
        st=st[index+1:]
        C1=True
if not P:
    if st.find('P')+1:
        index=st.find('P')
        st=st[index+1:]
        P=True
if not C2:
    if st.find('C')+1:
        C2=True


if U and C1 and P and C2:
    print("I love UCPC")
else:
    print("I hate UCPC")