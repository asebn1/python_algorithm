import utility

class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p

   
key=[" ","A","B","C","D"]
p=[0,0.375, 0.375, 0.125,0.125]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

#구현
for diagonal in range (1,n,1):
    for i in range(1,n-diagonal+1,1):
        j = i+diagonal
        sum = 0
        min = 10000
        for k in range (i,j+1,1):
            sum += p[k]
        for k in range (i,j+1,1):
            t = a[i][k-1] + a[k+1][j] + sum
            if (t<min):
                min = t
                a[i][j] = t
                r[i][j] = k
#

utility.printMatrixF(a)
print()
utility.printMatrix(r)

root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
