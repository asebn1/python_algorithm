import copy
r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))
# 공기청정기 위치
airboard = []
x = 0
for i in range(len(board)):
    if board[i][0] == -1:
        x = i
        break
airboard.append((x,0))
airboard.append((x+1,0))
# for i in board:
#     print(i)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def mise():
    global board
    temp_board = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            cnt = 0
            if board[i][j] == -1:
                continue
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                # 미세먼지 예외
                if not (0<=nx<r and 0<=ny<c):
                    continue
                if board[nx][ny] == -1:
                    continue
                # 확산
                cnt+=1
                temp_board[nx][ny] += board[i][j]//5
            temp_board[i][j] += (board[i][j] - (board[i][j]//5)*cnt)
    # 공기청정기 위치
    x1, y1 = airboard[0]
    temp_board[x1][y1] = -1
    x1, y1 = airboard[1]
    temp_board[x1][y1] = -1
    board = copy.deepcopy(temp_board)

# for i in board:
#     print(i)
# print()
def activeUp():
    global board
    # 위에서부터 -1찾기
    x = airboard[0][0]
    changeList = []
    # 왼쪽
    for i in range(x-1,-1,-1):
        changeList.append((i, 0))
    # 위
    for i in range(1, c):
        changeList.append((0, i))
    # 오른쪽
    for i in range(1, x):
        changeList.append((i, c-1))
    # 아래
    for i in range(c-1, 0, -1):
        changeList.append((x, i))
    # print(changeList)
    # 바꿈
    for i in range(len(changeList)-1):
        x1, y1 = changeList[i]
        x2, y2 = changeList[i+1]
        board[x1][y1] = board[x2][y2]
    # 초기 0
    x1, y1 = changeList[-1]
    board[x1][y1] = 0

def activeDown():
    global board
    # 위에서부터 -1찾기
    x = airboard[1][0]
    changeList = []
    # 왼쪽
    for i in range(x+1, r):
        changeList.append((i, 0))
    # 아래
    for i in range(1, c):
        changeList.append((r-1, i))
    # 오른쪽
    for i in range(r-2, x-1, -1):
        changeList.append((i, c-1))
    # 위
    for i in range(c-2, 0, -1):
        changeList.append((x, i))
    # print(changeList)
    # 바꿈
    for i in range(len(changeList)-1):
        x1, y1 = changeList[i]
        x2, y2 = changeList[i+1]
        board[x1][y1] = board[x2][y2]
    # 초기 0
    x1, y1 = changeList[-1]
    board[x1][y1] = 0
# mise()
# for i in board:
#     print(i)
# print()
#
# activeUp()
# for i in board:
#     print(i)
# activeDown()
# for i in board:
#     print(i)
for i in range(t):
    mise()
    activeUp()
    activeDown()
# 미세먼지
ret = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            continue
        ret += board[i][j]
print(ret)