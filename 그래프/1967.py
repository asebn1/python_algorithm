from collections import deque
n = int(input())
db = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,weight = map(int, input().split())
    db[a].append((b,weight))
    db[b].append((a,weight))


def bfs(s):
    q = deque()
    q.append((s, 0)) # 1
    visited = [False] * (n+1)
    visited[s] = True

    # 최대위치, 값 저장용
    result = [0,0]
    while q:
        d, w = q.popleft() # 1 0 
        for i in db[d]: # 2,3 / 3,2
            next_num = i[0]
            weight = i[1]
            if visited[next_num] == False:
                visited[next_num] = True
                q.append((next_num, w+weight))
                if result[1] < w+weight:
                    result[0] = next_num
                    result[1] = w+weight
    return result


print(bfs(bfs(1)[0])[1])
