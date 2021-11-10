import heapq
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b)) # 시간, 위치

def dijsktra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            next_d, next_now = i
            if distance[next_now] > d + next_d:
                distance[next_now] = d + next_d
                heapq.heappush(q, (d + next_d, next_now))
ret = 0
# x에 대한 거리
dijsktra(x)
distance_x = distance[:]
for i in range(1, n+1):
    if i == x:
        continue
    distance = [INF] * (n + 1)
    dijsktra(i)
    if ret < distance[x]+ distance_x[i]:
        ret = distance[x]+ distance_x[i]
print(ret)