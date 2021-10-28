import heapq


def dijkstra(graph, N):
    q = []
    INF = int(1e9)
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, 1))  # 현재 거리, start
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)  # 0, 1
        if distance[now] > dist:
            continue
        for i in graph[now]:
            next_dist, next_now = i
            if distance[next_now] > next_dist + dist:
                distance[next_now] = next_dist + dist
                heapq.heappush(q, (next_dist + dist, next_now))
    return distance


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for i in road:
        a, b, c = i[0], i[1], i[2]
        graph[a].append((c, b))
        graph[b].append((c, a))
    distance = dijkstra(graph, N)
    result = 0
    for i in distance:
        if i <= K:
            result += 1
    return result


"""
1~N  1에서 모두 걸리는 시간  <= K
"""