import utility
import queue
e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
           if j in e[i]:
              a[i][j]=1
              a[j][i]=1
utility.printMatrix(a)

visited =n*[0]
            
def BFS(a,v):
    q=queue.Queue()
    q.put(v) # q에 0 삽입.
    while q.empty() == False:
        x=q.get() # 0 가져옴
        print(x)
        visited[x]=1
        for y in range(0,n): #0~7
            if a[x][y] == 1 and visited[y] ==0: #a[0][0~7]
                q.put(y) # 1 2 3 
                visited[y]=1
                
BFS(a,0)


