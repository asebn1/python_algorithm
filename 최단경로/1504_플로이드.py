import heapq

n, e = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for i in range(e):
    # a -> b / b->a
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())


for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(min(graph[1][v1] + graph[v1][v2] + graph[v2][n], graph[1][v2] + graph[v2][v1] + graph[v1][n]))