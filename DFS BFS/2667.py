from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(0, n):
    graph.append(list(input()))

# bfs q
q =deque()
def bfs(graph):
    q.append((0,0))
    while q:
        y, x = q.popleft()
        if x-1 >= 0 and x-1 < m and graph[y][x-1] == '1':
            q.append((y, x-1))
            graph[y][x-1] = int(graph[y][x]) + 1
        if x+1 >= 0 and x+1 < m and graph[y][x+1] == '1':
            q.append((y, x+1))
            graph[y][x+1] = int(graph[y][x]) + 1
        if y-1 >= 0 and y-1 < n and graph[y-1][x] == '1':
            q.append((y-1, x))
            graph[y-1][x] = int(graph[y][x]) + 1
        if y+1 >= 0 and y+1 < n and graph[y+1][x] == '1':
            q.append((y+1, x))
            graph[y+1][x] = int(graph[y][x]) + 1


bfs(graph)
print(graph[n-1][m-1])