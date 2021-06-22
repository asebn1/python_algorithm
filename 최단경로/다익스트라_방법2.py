# 최단거리가 가장 짧은 노드 선택
# 시간복잡도 : LogN

# 사용법
"""
1. 출발 노드 설정
2. 최단 거리 테이블(T : 1차원 리스트) 초기화

3. 가장 짧은 노드 꺼내기. heapq 사용 (우선순위큐 사용)  / (visited 대체)
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산 -> 최단 거리 테이블(distance) 갱신

5. 3~4 반복 
"""
# 언제사용?
# 한 지점 -> 다른 특정 지점 [최단경로]

import heapq
INF = int(1e9) # 무한


# 노드 1~6번
# 입력 수 11번
n, m = 6, 11 
# 시작 노드번호
start = 1

# 1. 그래프
graph = [[] for _ in range(n+1)]
# 2. 최단 거리 테이블. 무한으로 초기화
distance = [INF] * (n+1)

# 정보받기
graph[1].append((2,2)) 
graph[1].append((3,5)) # 1->3 가는비용 : 5
graph[1].append((4,1))
graph[2].append((3,3))
graph[2].append((4,2))
graph[3].append((2,3))
graph[3].append((6,5))
graph[4].append((3,3))
graph[4].append((5,1))
graph[5].append((3,1))
graph[5].append((6,2))

print(graph)
# 다익스트라
def dijkstra(start):
    # 3. heapq
    q = []
    # 시작 노드로 가는 최단경로 0 / (0,1) 
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # q가 비어있지 않을때까지
    while q:
        # 가장 짧은 노드 정보 꺼내기
        # 0, 1
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 더 짧은 경우 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
# 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=' ')

# 헷갈리는 점
# 입력은 1 2 3  : 1 -> 2  비용 3
# q에는 (2, 3)  :   -> 3  비용 2