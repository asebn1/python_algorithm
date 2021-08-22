import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for i in range(e):
    # a -> b / b->a
    a,b,c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 0 2
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 0 2
        # if distance[now] < dist :
        #     continue
        for check_dist, check_now in graph[now]:  # 2번에서 갈 수 있는것
            if dist + check_dist < distance[check_now]:
                distance[check_now] = dist + check_dist
                heapq.heappush(q, (dist + check_dist, check_now))

result = []
result.append([])
for i in range(1, n+1):
    dijkstra(i)
    result.append(distance)
    distance = [INF] * (n+1)

print(min(result[1][v1] + result[v1][v2] + result[v2][n], result[1][v2] + result[v2][v1] + result[v1][n]))
