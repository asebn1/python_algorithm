from collections import deque
n, m = map(int, input().split())
board = []
board_len = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]
board_len = [[0]*m for _ in range(n)]

for i in range(n):
    board.append(list(input()))
## R위치
## B위치
r_x, r_y = 0, 0
b_x, b_y = 0, 0
end_x, end_y = 0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r_x, r_y = i, j
        if board[i][j] == 'B':
            b_x, b_y = i, j
        if board[i][j] == 'O':
            end_x, end_y = i, j

# bfs로 갈 수 있는지 찾기 -> 경로 찾기
q = deque()
q.append([r_x, r_y])
board_len[r_x][r_y] = 0
visited[r_x][r_y] = True
while q:
    x, y = q.popleft()
    # 상하좌우 확인
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if board[nx][ny]=='.' and visited[nx][ny] == False:
            q.append([nx, ny])
            board_len[nx][ny] = board_len[x][y] + 1
            visited[nx][ny] = True
        if board[nx][ny]=='O':
            board_len[nx][ny] = board_len[x][y] + 1
            visited[nx][ny] = True
            break
# 경로 찾기
locate = []
locate.append([end_x, end_y]) # 26 위치
check_num = board_len[end_x][end_y]-1 # 25
q = deque()
q.append([end_x, end_y])
while q:
    x, y = q.popleft()
    # 상하좌우 확인
    if check_num == 0:
        break
    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if board_len[nx][ny]==check_num:
            locate.append([nx, ny])
            q.append([nx, ny])
            check_num -= 1
            break
locate.append([r_x, r_y])
locate.reverse()
# print(locate)
# 경로 -> 방향리스트 / 개수 찾기
direction = []
for i in range(len(locate)-1):
    x,y = locate[i]
    next_x, next_y = locate[i+1]
    if x < next_x:
        if len(direction) > 0 and direction[-1] == 'down':
            continue
        else:
            direction.append('down')
    elif x > next_x:
        if len(direction) > 0 and direction[-1] == 'up':
            continue
        else:
            direction.append('up')
    elif y < next_y:
        if len(direction) > 0 and direction[-1] == 'right':
            continue
        else:
            direction.append('right')
    elif y > next_y:
        if len(direction) > 0 and direction[-1] == 'left':
            continue
        else:
            direction.append('left')


# 골인
r_goal, b_goal = False, False

def simu(r_b, direct):
    global r_x, r_y, b_x, b_y, r_goal, b_goal
    x, y = 0,0
    # 빨간색볼
    if r_b == 'R':
        x,y=r_x, r_y
    else:
        x,y=b_x, b_y
        
    board[x][y] = '.'
    # 최대 10
    if direct == 'left':
        for i in range(10):
            if board[x][y-1] == '.':
                y = y-1
            elif board[x][y-1] == 'O':
                y = y-1
                if r_b == 'R':
                    r_goal = True
                    r_y = y
                else:
                    b_goal = True
                    b_y = y
                break
            else:
                if r_b == 'R':
                    r_y = y
                else:
                    b_y = y
                break
    elif direct == 'right':
        for i in range(10):
            if board[x][y+1] == '.':
                y = y+1
            elif board[x][y+1] == 'O':
                y = y+1
                if r_b == 'R':
                    r_goal = True
                    r_y = y
                else:
                    b_goal = True
                    b_y = y
                break
            else:
                if r_b == 'R':
                    r_y = y
                else:
                    b_y = y
                break
    elif direct == 'up':
        for i in range(10):
            if board[x-1][y] == '.':
                x = x-1
            elif board[x-1][y] == 'O':
                x = x-1
                if r_b == 'R':
                    r_goal = True
                    r_x = x
                else:
                    b_goal = True
                    b_x = x
                break
            else:
                if r_b == 'R':
                    r_x = x
                else:
                    b_x = x
                break
    elif direct == 'down':
        for i in range(10):
            if board[x+1][y] == '.':
                x = x+1
            elif board[x+1][y] == 'O':
                x = x+1
                if r_b == 'R':
                    r_goal = True
                    r_x = x
                else:
                    b_goal = True
                    b_x = x
                break
            else:
                if r_b == 'R':
                    r_x = x
                else:
                    b_x = x
                break
    if x==end_x and y==end_y:
        board[x][y] = 'O'
    else:
        board[x][y] = r_b
        

# 시뮬레이션
for i in direction:
# left : R,B중 y좌표가 더 적은것 먼저 수행
    if i == 'left':
        if r_y < b_y:
            simu('R', 'left')
            simu('B', 'left')
        else:
            simu('B', 'left')
            simu('R', 'left')
# right : R,B중 y좌표가 더 큰것 먼저 수행
    if i == 'right':
        if r_y > b_y:
            simu('R', 'right')
            simu('B', 'right')
        else:
            simu('B', 'right')
            simu('R', 'right')
# up : R,B중 x좌표가 더 작은 것 먼저 수행
    if i == 'up':
        if r_x < b_x:
            simu('R', 'up')
            simu('B', 'up')
        else:
            simu('B', 'up')
            simu('R', 'up')
# down : R,B중 x좌표가 더 큰 것 먼저 수행
    if i == 'down':
        if r_x > b_x:
            simu('R', 'down')
            simu('B', 'down')
        else:
            simu('B', 'down')
            simu('R', 'down')
# print(direction)
# for i in board_len:
#     print(i)
if len(direction) >= 11:
    print(-1)
elif r_goal == True and b_goal == True:
    print(-1)
elif r_goal == True:
    print(len(direction))
else:
    print(-1)