from itertools import combinations
import copy
n, m = map(int, input().split())
graph = []
for _ in range(0, n):
    graph.append(list(input().split(' ')))
arrCase = []
for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == '0':
            arrCase.append((i, j))

# dfs
def dfs(graph, v):
    a, b = v[0], v[1] # a는 y축, b는 x축
    if graph[a][b] != '2':
        return
    # 범위 체크, 0 이면
    if a+1 >= 0 and a+1 < n and graph[a+1][b]=='0':
        graph[a+1][b]='2'
        dfs(graph, (a+1, b))

    if a-1 >= 0 and a-1 < n and graph[a-1][b]=='0':
        graph[a-1][b]='2'
        dfs(graph, (a-1, b))

    if b+1 >= 0 and b+1 < m and graph[a][b+1]=='0':
        graph[a][b+1]='2'
        dfs(graph, (a, b+1))
    
    if b-1 >= 0 and b-1 < m and graph[a][b-1]=='0':
        graph[a][b-1]='2'
        dfs(graph, (a, b-1))

## 3가지 경우의 수 뽑기
threeCase = list(combinations(arrCase, 3))
max = 0
for i in threeCase:
    test = copy.deepcopy(graph)
    a,b,c = i
    test[int(a[0])][int(a[1])] = '1'
    test[int(b[0])][int(b[1])] = '1'
    test[int(c[0])][int(c[1])] = '1'

    # dfs
    for a in range(0, n):
        for b in range(0, m):
            dfs(test, (a, b))
    # 0의 개수 count
    count = 0
    for i in test:
        count += i.count('0')
    if max < count:
        max = count
print(max)