from collections import deque
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs
def bfs(x, y):
    if board[x][y] == 0:
        return False
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<n and 0<=ny<m):
                continue
            if board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = 0
    return True
testCase = int(input())
for case in range(testCase):
    # 입력
    n, m, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    ret = 0
    for i in range(n):
        for j in range(m):
            if bfs(i, j):
                ret += 1
    print(ret)