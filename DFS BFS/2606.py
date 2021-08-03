n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
for i in range(0, k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [False] * (n+1)
# bfs
def bfs(graph, s, visited):
    visited[s] = True
    for i in graph[s]: # 2 3 5 6
        if visited[i] == False:
            visited[i] = True
            bfs(graph, i, visited)
bfs(graph, 1, visited)
print(visited.count(True)-1)