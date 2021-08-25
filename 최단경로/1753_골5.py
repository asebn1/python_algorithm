import heapq
# 다익스트라 
# 1개의 점에서 가는 최단경로 수

# 입력
v, e = map(int, input().split())
k = int(input())
# 초기
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
# 입력
for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
for i in graph:
    print(i)
# 다익스트라 구현
# 1개의 점
def dijkstra(start):
    q = []
    # q에 1개 초기화
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 0, 1
        if distance[now] < dist:
            continue
        for check_d, check_now in graph[now]:
            if dist + check_d < distance[check_now]:
                distance[check_now] = dist + check_d
                heapq.heappush(q, (dist+check_d, check_now))

dijkstra(1)
print(distance)