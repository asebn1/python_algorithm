from collections import deque
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
# 상어 x, y
x, y = 0, 0
sharkSize = 2
# 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x, y = i, j
            board[i][j] = 0

def bfs(check_board, x, y):
    q = deque()
    q.append([0, x, y])
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    while q:
        dist, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 나감
            if not (0<=nx<n and 0<=ny<n):
                continue
            # 큰 상어는 지나갈 수 없다
            elif board[nx][ny] > sharkSize:
                continue
            # 방문했으면
            elif visited[nx][ny] == True:
                continue
            # 물고기를 먹을 수 있으면
            if board[nx][ny] < sharkSize and board[nx][ny] != 0:
                if len(check_board) > 0 and check_board[0][0] < dist+1:
                    return
                check_board.append([dist+1, nx, ny])
                visited[nx][ny] = True
            # 지나가기
            else:
                visited[nx][ny] = True
                q.append([dist+1, nx, ny])

ret = 0
eat_count = 0
while 1:
    check_board = []
    bfs(check_board, x, y)
    if len(check_board) == 0:
        break
    check_board = sorted(check_board, key=lambda x : (x[0], x[1], x[2]))
    eat_count += 1
    if eat_count == sharkSize:
        sharkSize += 1
        eat_count = 0
    dist, t1, t2 = check_board[0]
    x, y = t1, t2
    board[x][y] = 0
    ret += dist
    # print(check_board)
print(ret)

