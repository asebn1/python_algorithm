# 다익스트라 Dijkstra

# 언제사용?
# 한 지점 -> 다른 특정 지점 [최단경로]

# 사용법
"""
1. 출발 노드 설정
2. 최단 거리 테이블(T : 1차원 리스트) 초기화
3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택
4. 해달 노드를 거쳐 다른 노드로 가는 비용 계산 -> 최단 거리 테이블(T) 갱신
5. 3~4 반복 (한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾음)
"""
# 방법 2가지
# 1. 구현 쉬움   / 동작 느림
# 2. 구현 어려움 / 동작 빠름
# 방법 2를 이해하고 정확히 구현하기

"""
- 방법 1 -
시간복잡도 V^2
"""

import sys
INF = int(1e9) # 무한

# 노드 1~6번
# 입력 수 11번
n, m = 6, 11 
# 시작 노드번호
start = 1
# 그래프
graph = [[] for _ in range(n+1)]
# 1. 방문학 적 있는지 체크
visited = [False] * (n+1)
# 2. 최단 거리 테이블. 무한으로 초기화
distance = [INF] * (n+1)
# 그래프 입력
graph[1].append((2,2)) 
graph[1].append((3,5)) # 1->3 가는시간 : 5
graph[1].append((4,1))
graph[2].append((3,3))
graph[2].append((4,2))
graph[3].append((2,3))
graph[3].append((6,5))
graph[4].append((3,3))
graph[4].append((5,1))
graph[5].append((3,1))
graph[5].append((6,2))

# 함수 1 
# 방문하지 않은 노드 중, 가장 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 거리가 가장 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 함수 2
# 다익스트라
def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # distance : [1000000000, 0, 2, 5, 1, 1000000000, 1000000000]

    for i in range(n-1):
        # 현재 가장 짧은 노드 찾기 -> 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

# 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=' ')
