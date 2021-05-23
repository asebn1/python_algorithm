n, m, t = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
t_list = []
for i in range(t):
    x,d,k = map(int, input().split())
    t_list.append((x-1, d, k))

# 반시계
def up(x):
    global board
    start = board[x][0]
    for i in range(0, len(board[x])-1):
        board[x][i] = board[x][i+1]
    board[x][-1] = start
# 시계
def down(x):
    global board
    end = board[x][-1]
    for i in range(len(board[x])-1, 0, -1):
        board[x][i] = board[x][i-1]
    board[x][0] = end
# 제거
def remove():
    global board
    visited = [[False]*m for _ in range(n)]
    check = False
    # 같은 원판
    for i in range(n):
        for j in range(-1, m - 1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i][j + 1]:
                visited[i][j] = True
                visited[i][j+1] = True
                check = True
    # 다른 원판
    for i in range(m):
        for j in range(n-1):
            if board[j][i] == 0:
                continue
            if board[j][i] == board[j+1][i]:
                visited[j][i] = True
                visited[j+1][i] = True
                check = True
    # 인접한 수 있음
    if check == True:
        for i in range(n):
            for j in range(m):
                if visited[i][j] == True:
                    board[i][j] = 0
    # 인접한 수 없음
    else:
        cnt = 0
        value = 0
        for a in range(n):
            for b in range(m):
                if board[a][b] != 0:
                    cnt += 1
                    value += board[a][b]
        # 인접한 수 없음
        if cnt != 0:
            avg = value/cnt
            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0:
                        # 평균보다 큰수 -1
                        # print(avg)
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1


for i in range(len(t_list)):
    x, d, k = t_list[i]
    temp_x = x
    while 1:
        # for i in board:
        #     print(i)
        # print()
        # print(temp_x)
        for j in range(k):
            if d == 0:
                down(temp_x)
            else:
                up(temp_x)
        temp_x += (x+1)
        if temp_x >= n:
            break
    remove()

# for i in board:
#     print(i)
# print()
ret = 0
for i in board:
    ret += sum(i)
print(ret)