import heapq

# 무한
INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 1))
    distance[start] = 0

    while q:
        # 0, 1
        a, target = heapq.heappop(q)
        if distance[target] < a:
            continue
        for i in graph[target]:
            # 0 + 4
            cost = distance[target] + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
dijkstra(start)
cnt = 0
for i in range(n+1):
    if distance[i] == INF:
        distance[i] = -1
    if distance[i] > 0:
        cnt += 1
print(cnt, max(distance))