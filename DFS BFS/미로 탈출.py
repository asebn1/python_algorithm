from collections import deque
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    arr[i] = (list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue    
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

    return arr[n-1][m-1]
    
    
print(arr)
print(bfs(0,0))
print(arr)