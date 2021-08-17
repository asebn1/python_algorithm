from collections import deque


def bfs(start, graph, n):
    q = deque()
    visited = [False] * (n + 1)
    visited[start[1]] = True
    q.append(start[1])

    while q:
        pop = q.popleft()
        for i in graph[pop]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
    return abs(visited.count(False) - 1 - visited.count(True))


def solution(n, wires):
    min = int(1e9)
    for w in range(0, len(wires)):
        test = []
        for j in range(0, len(wires)):
            if w == j:
                continue
            test.append(wires[j])
        ## 다른 wires
        graph = [[] for _ in range(n + 1)]
        for i in test:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        check_num = bfs(test[0], graph, n)

        if min > check_num:
            min = check_num
    return min