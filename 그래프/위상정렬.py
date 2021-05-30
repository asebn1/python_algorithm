from collections import deque
# 노드 7, 8번 입력
v, e = 7, 8
# 진입차수 0 초기화
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

graph[1].append(2)
graph[1].append(5)
graph[2].append(3)
graph[2].append(6)
graph[3].append(4)
graph[4].append(7)
graph[5].append(6)
graph[6].append(4)
indegree[2] += 1
indegree[5] += 1
indegree[3] += 1
indegree[6] += 1
indegree[4] += 1
indegree[7] += 1
indegree[6] += 1
indegree[4] += 1

# 위상정렬함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작시 집입차수 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()