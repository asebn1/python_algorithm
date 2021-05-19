from collections import defaultdict
r, c, k = map(int, input().split())
board = []
for i in range(3):
    board.append(list(map(int, input().split())))

# 1번 r정렬
def play_r():
    global board
    temp_board = []
    max_len = 0
    for i in board:
        db = defaultdict(int)
        q = []
        # db에 값 추가
        for j in i:
            if j == 0:
                continue
            db[j] += 1
        # q에 추가
        for j in db.keys():
            q.append((j, db[j]))
        q.sort(key=lambda x : (x[1], x[0]))
        temp = []
        for i in q:
            temp += list(i)
        temp_board.append(temp)
        if max_len < len(temp):
            max_len = len(temp)
    # 0 채우기
    board = [[0]*max_len for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(max_len):
            if len(temp_board[i]) > j:
                board[i][j] = temp_board[i][j]
            else:
                board[i][j] = 0
def changeBoard():
    global board
    x = len(board[0]) # 6
    y = len(board) # 3
    temp_board = [[0]*y for _ in range(x)]
    for i in range(y):
        for j in range(x):
            temp_board[j][i] = board[i][j]
    # for i in temp_board:
    #     print(i)
    board = temp_board

def play_c():
    changeBoard()
    play_r()
    changeBoard()

check = False
cnt = 0
while 1:
    # 범위 내
    if 0<= r-1 < len(board) and 0<= c-1 < len(board[0]):
        if board[r-1][c-1] == k:
            check = True
            break
    if len(board) >= len(board[0]):
        play_r()
    else:
        play_c()
    # for i in board:
    #     print(i)
    # print()
    cnt += 1
    if cnt == 101:
        break
if check == False:
    print(-1)
else:
    print(cnt)