# 언제사용?
# 모든지점 -> 모든지점 [최단경로]
# 시간복잡도 N^3
# 결과 distance(graph)가 2차원

# 사용법
"""
1. 자기 자신 가는 비용 0 초기화 / 각 간선 정보 받아 초기화
2. 플로이드 워셜 알고리즘 수행
for k a b
 : graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

"""
INF = int(1e9) # 무한

# 노드 총 4개
# 입력 7개
n, m = 4, 7
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신 비용 0 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선 정보 입력 초기화
graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][2] = 2

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()