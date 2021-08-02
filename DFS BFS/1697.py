from collections import deque
S = 100001
visited = [False] * S
graph = [0] * S

n, k = map(int, input().split())
q = deque()
# bfs
def bfs(graph, n, visited):
    q.append(n)
    visited[n] = True
    while q:
        pop = q.popleft()
        if pop == k:
            break
        if pop*2 >= 0 and pop*2 <= S-1:
            if visited[pop*2] == False:
                visited[pop*2] = True
                graph[pop*2] = graph[pop] + 1
                q.appendleft(pop*2)
        if pop-1 >= 0 and pop-1 <= S-1:
            if visited[pop-1] == False:
                visited[pop-1] = True
                graph[pop-1] = graph[pop] + 1
                q.append(pop-1)
        if pop+1 >= 0 and pop+1 <= S-1:
            if visited[pop+1] == False:
                visited[pop+1] = True
                graph[pop+1] = graph[pop] + 1
                q.append(pop+1)
bfs(graph, n, visited)
print(graph[k])