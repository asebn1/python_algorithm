import copy
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
check_board = []
groups = []
def bfs(start):
    global groups
    q = []
    x,y= start
    q.append((x,y))
    temp_group = []
    while q:
        x1, y1 = q.pop(0)
        # 만약 groups에 추가된 적 있으면 x
        if len(groups) > 0:
            for g in groups:
                if (x1, y1) in g:
                    return
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if not (0<=nx<n and 0<=ny<n) :
                continue
            # 범위 내에 속하면 값 넣기
            if l <= abs(board[x1][y1] - board[nx][ny]) <= r:
                # 아예 없으면 추가
                if len(temp_group) == 0:
                    q.append((nx, ny))
                    temp_group.append((x1, y1))
                    temp_group.append((nx, ny))
                # (nx, ny)만 없으면 추가
                if (nx, ny) not in temp_group:
                    q.append((nx, ny))
                    temp_group.append((nx, ny))
    temp_group.sort()
    # print(temp_group)
    if temp_group not in groups and len(temp_group)>1:
        groups.append(temp_group)
    # print(temp_group)
    # groups.append(temp_group)

# for i in board:
#     print(i)
# print()
ret = 0
while 1:
    groups = []
    for i in range(n):
        for j in range(n):
            bfs((i, j))
    if len(groups) == 0:
        break
    for g in groups:
        sums = 0
        for j in g:
            x, y = j
            sums += board[x][y]
        avgs = sums//len(g)
        # 값 넣기
        for j in g:
            x, y = j
            board[x][y] = avgs
    # for g in groups:
    #     print(g)
    # for i in board:
    #     print(i)
    # print()
    ret += 1
print(ret)
