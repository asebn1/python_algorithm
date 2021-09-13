import heapq

INF = int(1e9)  # 무한 값


# 다익스트라 구현, 특정위치 포함
def dijkstra(start, graph, n, s, a, b, fares):
    # 1. distance(목표) 초기화
    distance = [INF] * (n + 1)
    distance[start] = 0

    # 2-1 heap 초기화
    q = []
    heapq.heappush(q, (0, start))  # (value, dst)

    # 2-2 while
    while q:
        # heappop
        value, dst = heapq.heappop(q)

        # distance 비교
        if distance[dst] < value:
            continue

        # graph
        for d, v in graph[dst]:
            next_value = value + v
            if distance[d] > next_value:
                distance[d] = next_value
                heapq.heappush(q, (next_value, d))  # (value, dst)

    # distance 리턴!
    return distance


def solution(n, s, a, b, fares):
    # 조건 : graph 구현
    graph = [[] for _ in range(n + 1)]
    for src, dst, value in fares:
        graph[src].append((dst, value))
        graph[dst].append((src, value))  # 거리 같음

    # 최단 경로 구하기
    dp = [[]] + [dijkstra(i, graph, n, s, a, b, fares) for i in range(1, n + 1)]

    answer = INF
    for i in range(1, n + 1):
        temp = dp[s][i] + dp[i][a] + dp[i][b]
        answer = min(answer, temp)

    return answer