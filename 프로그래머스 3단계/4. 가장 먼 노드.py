from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for i in edge:
        a, b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)

    cnt = [0] * (n + 1)

    def dijkstra(s):
        visited = [False] * (n + 1)
        q = deque()
        q.append((0, 1))  # 거리, 위치
        visited[1] = True
        while q:
            d, now = q.popleft()
            for next_now in graph[now]:
                if visited[next_now] == False:
                    q.append((d + 1, next_now))
                    cnt[d + 1] += 1
                    visited[next_now] = True
        print(cnt)

    dijkstra(1)
    for i in range(len(cnt) - 1, -1, -1):
        if cnt[i] != 0:
            return cnt[i]