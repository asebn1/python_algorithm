def allShortestPath(g,n):
    d = g
    p = [[0 for cols in range(n)] for rows in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(d[i][j] > d[i][k]+d[k][j]):
                    d[i][j] = d[i][k] + d[k][j] #최단경로. [0][2] = [0][3] + [3][2]
                    p[i][j] = k+1 #가능한 경로 저장. 1->3에 4가 가능하다. k=3
    return d,p
                    
def printMatrix(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()
        
def path(p, q, r):
    print("v%d"% q, end=" ")
    _path(p, q - 1, r - 1)
    print("v%d"% r, end=" ")

def _path(p, q, r):
    if(p[q][r] != 0):
        _path(p,q,p[q][r]-1)
        print("v%d"%p[q][r], end=" ")
        _path(p,p[q][r]-1, r)


inf=1000
g=[[0,1,inf, 1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]
printMatrix(g) # 그래프의 인접 행렬 거리
d, p = allShortestPath(g,5) # 5*5행렬
print()
printMatrix(d) #각 정점들 사이의 최단 거리
print()
printMatrix(p) #가능한 최단경로 쉽게 확인
print()       
path(p, 5, 3) #경로 출력 5->3
