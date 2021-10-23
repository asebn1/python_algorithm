from collections import deque


def bfs(board):
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 초과시 나가기
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            # 0일경우 나가기
            if board[nx][ny] == 0:
                continue
            # 방문한 적 없는 곳만
            if visited[nx][ny] == True:
                continue
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1
            visited[nx][ny] = True


def solution(maps):
    bfs(maps)
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]