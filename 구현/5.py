
# 입력
n,m, x,y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
doit = list(map(int, input().split()))
# print(board)
# print(doit)
dice = [0]*6

# 동서북남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in doit:
    d = i-1
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    x = nx
    y = ny
    # 동
    if d == 0:
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
    # 서
    elif d == 1:
        dice[1], dice[3], dice[5], dice[4] = dice[5], dice[4], dice[3], dice[1]
    # 북
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    # 남
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

    if board[x][y]==0:
        board[x][y] = dice[3]
        # dice[3] = 0
    else:
        dice[3] = board[x][y]
        board[x][y] = 0
    print(dice[1])
