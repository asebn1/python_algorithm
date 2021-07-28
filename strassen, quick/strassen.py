from numpy import *

def strassen(n,A,B,C):
    t = 2
    #col의 범위, row의 범위
    a1 = array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    a2 = array([[A[rows][cols] for cols in range(int(n/2), n)]for rows in range(int(n/2))])
    a3 = array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2), n)])
    a4 = array([[A[rows][cols] for cols in range(int(n/2), n)]for rows in range(int(n/2), n)])
    b1 = array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    b2 = array([[B[rows][cols] for cols in range(int(n/2), n)]for rows in range(int(n/2))])
    b3 = array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2), n)])
    b4 = array([[B[rows][cols] for cols in range(int(n/2), n)]for rows in range(int(n/2), n)])

    if(n <= t):
        C = array(A)@array(B)
    else:        
        m1=m2=m3=m4=m5=m6=m7=m8=[]
        strassen(int(n/2), a1+a2, b1+b4, m1)
        strassen(int(n/2), a3+a4, b1, m2)
        strassen(int(n/2), a1, b2-b4, m3)
        strassen(int(n/2), a4, b3-b1, m4)
        strassen(int(n/2), a1+a2, b4, m5)
        strassen(int(n/2), a3-a1, b1+b2, m6)
        strassen(int(n/2), a2-a4, b3+b4, m7)
        C = [array(m1)+array(m4)-array(m5)+array(m7), array(m3)+array(m5), array(m2)+array(m4)
             , array(m1)+array(m3)-array(m2)+array(m6)]

n = 4
A = [[5 for cols in range(n)]for rows in range(n)]
B = [[7 for cols in range(n)]for rows in range(n)]
C = array(A)@array(B)
print(C)
strassen(n,A,B,C)
print(C)
