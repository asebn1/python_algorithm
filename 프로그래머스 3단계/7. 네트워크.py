from collections import deque


def solution(n, computers):
    db = computers
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if db[i][j] == 1:
                graph[i].append(j)
    # print(graph)
    # 갈 수 있으면 체크
    visited = [False] * n

    def solv(idx):
        q = deque()
        if visited[idx] == True:
            return 0
        q.append(idx)
        while q:
            pop = q.popleft()
            for i in graph[pop]:  # 0,1
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
        return 1

    answer = 0
    for i in range(n):
        # print(visited)
        if solv(i):
            answer += 1
    return answer


"""
[1, 1, 0]
[1, 1, 1]
[0, 1, 1]

"""