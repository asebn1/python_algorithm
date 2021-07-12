import utility

def order(p,i,j):
    if i==j:
        print("A",i,end="")
    else:
        k = p[i][j]
        print("(",end="")
        order(p,i,k)
        order(p,k+1,j)
        print(")",end="")
         
d=[5,2,3,4,6,7,8]
n=len(d)-1 #6

m=[[0 for j in range(1,n+2)] for i in range(1,n+2)] #7*7
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

for diagonal in range(1, n, 1): #1, 6, 1
    for i in range(1, n-diagonal+1, 1): # 1, 6, 1/2, 5, 1 /3, 4, 1
        j = i + diagonal
        minn = 10000
        for k in range(i,j,1):
            t = m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
            if(t < minn):
                minn = t
                m[i][j] = t
                p[i][j] = k
        



utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6) # (A 1((((A 2A 3)A 4)A 5)A 6))
