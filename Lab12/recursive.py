'''
Two natural numbers m and n are given. Display in all possible modalities the numbers from 1
to n, such that between any two numbers on consecutive positions, the difference in absolute
value is at least m. If there is no solution, display a message.
'''
#recursive


def valid(st,m,k):
    if k==0:
        return True
    for i in range(0,k):
        if st[i]==st[k]:
            return False
    if abs(st[k]-st[k-1])<m:
        return False
    return True

def bkt(st,n,m,k):
    for i in range(1,n+1):
        st[k]=i
        if valid(st,m,k):
            if k==n-1:
                print(st)
            else:
                bkt(st,n,m,k+1)

n=int(input("n="))
m=int(input("m="))
if n==1:
    st=[1]
    print(st)
elif n//2<m:
    print('There is no solution.')
else:
    st=[None]*n
    bkt(st,n,m,0)