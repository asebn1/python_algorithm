import copy
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# dfs로 2 채우기
def dfs(start, temp_board):
    x, y = start
    if temp_board[x][y] != 2:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<m):
            continue
        if temp_board[nx][ny] == 0:
            temp_board[nx][ny] = 2
            dfs((nx, ny), temp_board)
# 0 위치 찾기
idx_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            idx_list.append((i, j))
# 3개 뽑기 조합으로
s = []
combi = []
def three(start):
    if len(s) == 3:
        combi.append(s.copy())
        return
    for i in range(start, len(idx_list)):
        if idx_list[i] in s:
            continue
        s.append(idx_list[i])
        three(i+1)
        s.pop()
three(0)

maxs = 0
# 바이러스 퍼트리기
for c in combi:
    t1, t2, t3 = c
    temp_board = copy.deepcopy(board)
    temp_board[t1[0]][t1[1]] = '1'
    temp_board[t2[0]][t2[1]] = '1'
    temp_board[t3[0]][t3[1]] = '1'
    for i in range(n):
        for j in range(m):
            dfs((i,j), temp_board)
    # 안전영역
    temp_max = 0
    for i in temp_board:
        temp_max += i.count(0)
    if temp_max > maxs:
        maxs = temp_max
print(maxs)
# print(board)