import heapq
v, e = map(int, input().split())
start = int(input())

INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a,b,c = map(int, input().split()) # 출발, 도착, 거리
    graph[a].append((c, b)) # 거리, 도착

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        # 확인
        if distance[now] < d:
            continue
        for next_d, next_now in graph[now]: # (2, 2), (3, 3)
            if distance[next_now] > d+next_d:
                distance[next_now] = d + next_d
                heapq.heappush(q, (d + next_d, next_now))
dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])