INF = int(1e9) # 무한

# 노드 총 5개
# 입력 7개
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신 비용 0 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선 정보 입력 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X, K 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])