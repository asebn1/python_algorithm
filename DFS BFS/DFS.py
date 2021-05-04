# DFS (Depth-First Search) : 깊이우선탐색 / 깊은 부분을 우선적으로 탐색
# 사용법 : 재귀
# 언제사용? : 나눠진 구역 구하기
def dfs(graph, v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드에서 연결된 다른 노드들 재귀적으로 방문
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * 9
dfs(graph, 1, visited)  