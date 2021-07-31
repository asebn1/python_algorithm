from collections import deque
# 초기화
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(0, m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

# bfs는 재귀
def bfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True 
    # 2 3 4
    for i in graph[start]:
        if visited[i] == False:
            bfs(graph, i, visited)

# dfs는 deque

q = deque()
def dfs(graph, v, visited):
    q.append(v)
    visited[v] = True
    while q:
        pop = q.popleft() # 1
        print(pop, end=' ')
        for i in graph[pop]: # 2 3 4
            if visited[i] == False:
                visited[i] = True
                q.append(i)


bfs(graph, v, visited)
print()
visited = [False] * (n+1)
dfs(graph, v, visited)
