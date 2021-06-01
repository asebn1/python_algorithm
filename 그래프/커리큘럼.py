from collections import deque
import copy
n = int(input())
# 차수
indegree = [0] * (n+1)
# 그래프
graph = [[] for i in range(n+1)]
# 걸리는 시간
time = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬함수
def topology_sort():
    # 이렇게 해야 기존 time 값이 변경안됨
    result = copy.deepcopy(time)
    q = deque()
    # 진입차수 0인것 삽입
    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        #
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, n+1):
        print(result[i])

topology_sort()