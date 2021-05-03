from collections import deque

# BFS(Breadth First Search) : 너비 우선 탐색 / 가까운 노드부터 탐색
# 사용법
# 1. Queue 구현을 위한 deque 사용 : popleft
# 2. 반복 (재귀X) : Queue가 끝날때까지

# 언제 사용?
# 최단경로
def bfs(graph, start, visited):
    a = deque([start])
    visited[start] = True
    while a:
        v = a.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                a.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],    # q에 2, 3, 8 넣음
    [1, 7],       # q의 2를 popleft, 1, 7 넣음
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * 9
bfs(graph, 1, visited)