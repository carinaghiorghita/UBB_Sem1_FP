'''
Two natural numbers m and n are given. Display in all possible modalities the numbers from 1
to n, such that between any two numbers on consecutive positions, the difference in absolute
value is at least m. If there is no solution, display a message.
'''

#iterative

def valid(st,m,k):
    if k==0:
        return True
    for i in range(0,k):
        if st[i]==st[k]:
            return False
    if abs(st[k]-st[k-1])<m:
        return False
    return True

def bkt(n,m):
    st=[None]*n
    k=0
    st[k]=0
    while k>=0:
        if st[k]<n:
            st[k]+=1
            if valid(st,m,k):
                if k==n-1:
                    print(st)
                else:
                    k+=1
                    st[k]=0
        else:
            k-=1

n=int(input("n="))
m=int(input("m="))
if n==0 or m==0:
    print('There is no solution.')
elif n==1:
    st=[1]
    print(st)
elif n//2<m:
    print('There is no solution.')
else:
    st=[None]*n
    bkt(n,m)