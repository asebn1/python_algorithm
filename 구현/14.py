from collections import deque
import copy
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
cctv_list = []
for i in range(n):
    for j in range(m):
        if 1<= board[i][j] <= 5:
            cctv_list.append((board[i][j], (i, j)))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# print(cctv_list)

mins = n*m
def bfs():
    global mins
    q = deque()
    temp_board = copy.deepcopy(board)
    q.append((temp_board, 0)) # [(1, (2, 2))]

    # up 감시
    def up(temp_board, x, y):
        nx = x
        ny = y
        board_trans = False
        while 1:
            nx += dx[0]
            ny += dy[0]
            # 범위 내 X
            if not (0 <= nx < n and 0 <= ny < m):
                break
            # 빈공간이거나 cctv 비추는곳
            if temp_board[nx][ny] == 0 or temp_board[nx][ny] == '#':
                board_trans = True
                temp_board[nx][ny] = '#'
            elif temp_board[nx][ny] == 6:
                break
        return board_trans
    #
    def down(temp_board, x, y):
        nx = x
        ny = y
        board_trans = False
        while 1:
            nx += dx[1]
            ny += dy[1]
            # 범위 내 X
            if not (0 <= nx < n and 0 <= ny < m):
                break
            # 빈공간이거나 cctv 비추는곳
            if temp_board[nx][ny] == 0 or temp_board[nx][ny] == '#':
                board_trans = True
                temp_board[nx][ny] = '#'
            elif temp_board[nx][ny] == 6:
                break
        return board_trans
    #
    def left(temp_board, x, y):
        nx = x
        ny = y
        board_trans = False
        while 1:
            nx += dx[2]
            ny += dy[2]
            # 범위 내 X
            if not (0 <= nx < n and 0 <= ny < m):
                break
            # 빈공간이거나 cctv 비추는곳
            if temp_board[nx][ny] == 0 or temp_board[nx][ny] == '#':
                board_trans = True
                temp_board[nx][ny] = '#'
            elif temp_board[nx][ny] == 6:
                break
        return board_trans
    #
    def right(temp_board, x, y):
        nx = x
        ny = y
        board_trans = False
        while 1:
            nx += dx[3]
            ny += dy[3]
            # 범위 내 X
            if not (0 <= nx < n and 0 <= ny < m):
                break
            # 빈공간이거나 cctv 비추는곳
            if temp_board[nx][ny] == 0 or temp_board[nx][ny] == '#':
                board_trans = True
                temp_board[nx][ny] = '#'
            elif temp_board[nx][ny] == 6:
                break
        return board_trans
    # print(cctv_list)
    while q:
        # 값 받기
        temp_board, idx = q.popleft()
        # for i in temp_board:
        #     print(i)
        # print()
        # cctv 다 검사했을 때 최소값
        if idx == len(cctv_list):
            # for i in temp_board:
            #     print(i)
            # print()
            temp_n = 0
            for i in temp_board:
                temp_n += i.count(0)
            if mins > temp_n:
                mins = temp_n
            continue

        cctv_num, temp = cctv_list[idx]
        x, y = temp
        # 1번 cctv
        if cctv_num == 1:
            # 상
            send_board = copy.deepcopy(temp_board)
            up(send_board, x, y)
            q.append((send_board, idx + 1))
            # 하
            send_board = copy.deepcopy(temp_board)
            down(send_board, x, y)
            q.append((send_board, idx + 1))
            # 좌
            send_board = copy.deepcopy(temp_board)
            left(send_board, x, y)
            q.append((send_board, idx + 1))
            # 우
            send_board = copy.deepcopy(temp_board)
            right(send_board, x, y)
            q.append((send_board, idx + 1))

        # 2번 cctv
        if cctv_num == 2:
            # 상, 하
            send_board = copy.deepcopy(temp_board)
            c1 = up(send_board, x, y)
            c2 = down(send_board, x, y)
            q.append((send_board, idx + 1))
            # 좌, 우
            send_board = copy.deepcopy(temp_board)
            c1 = left(send_board, x, y)
            c2 = right(send_board, x, y)
            q.append((send_board, idx + 1))

        # 3번 cctv
        if cctv_num == 3:
            # ㄴ
            send_board = copy.deepcopy(temp_board)
            c1 = up(send_board, x, y)
            c2 = right(send_board, x, y)
            q.append((send_board, idx + 1))
            # r
            send_board = copy.deepcopy(temp_board)
            c1 = right(send_board, x, y)
            c2 = down(send_board, x, y)
            q.append((send_board, idx + 1))
            # r
            send_board = copy.deepcopy(temp_board)
            c1 = down(send_board, x, y)
            c2 = left(send_board, x, y)
            q.append((send_board, idx + 1))
            # r
            send_board = copy.deepcopy(temp_board)
            c1 = left(send_board, x, y)
            c2 = up(send_board, x, y)
            q.append((send_board, idx + 1))
        # 4번 cctv
        if cctv_num == 4:
            #
            send_board = copy.deepcopy(temp_board)
            c1 = up(send_board, x, y)
            c2 = right(send_board, x, y)
            c3 = left(send_board, x, y)
            q.append((send_board, idx + 1))
            #
            send_board = copy.deepcopy(temp_board)
            c1 = up(send_board, x, y)
            c2 = right(send_board, x, y)
            c3 = down(send_board, x, y)
            q.append((send_board, idx + 1))
            #
            send_board = copy.deepcopy(temp_board)
            c1 = down(send_board, x, y)
            c2 = right(send_board, x, y)
            c3 = left(send_board, x, y)
            q.append((send_board, idx + 1))
            #
            send_board = copy.deepcopy(temp_board)
            c1 = up(send_board, x, y)
            c2 = down(send_board, x, y)
            c3 = left(send_board, x, y)
            q.append((send_board, idx + 1))
        if cctv_num == 5:
            #
            send_board = copy.deepcopy(temp_board)
            up(send_board, x, y)
            down(send_board, x, y)
            right(send_board, x, y)
            left(send_board, x, y)
            q.append((send_board, idx + 1))
bfs()
print(mins)
