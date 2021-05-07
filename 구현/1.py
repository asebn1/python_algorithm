import copy
n = int(input())
board = []
for i in range(n):
    m = list(map(int, input().split()))
    board.append(m)
# print(board)

# 상하좌우 5번 list
check_list = []
s = []

def dfs():
    if len(s) == 5:
        check_list.append(s.copy())
        return
    for i in range(0, 4):
        s.append(i)
        dfs()
        s.pop()
dfs()

# 상하좌우 1024번 돌림
def left(board):
    for i in board:
        for j in range(0, len(i)-1): #0,1 / 2 2 2
            for k in range(j+1, n):
                if i[j] == 0:
                    break
                if i[j] != i[k] and i[k] != 0:
                    break
                if i[j] == i[k]:
                    i[j] += i[k]
                    i[k] = 0
                    break
    # 왼쪽으로 밀기
    for i in range(n):
        q = []
        for j in range(0, n):
            if board[i][j] != 0:
                q.append(board[i][j])
                board[i][j] = 0

        for j in range(0, n):
            if len(q) != 0:
                board[i][j] = q.pop(0)
            else:
                break


def right(board):
    # reverse
    for i in range(n):
        board[i].reverse()
    # print(board)
    for i in board:
        for j in range(0, len(i)-1): #0,1 / 2 2 2
            for k in range(j+1, n):
                if i[j] == 0:
                    break
                if i[j] != i[k] and i[k] != 0:
                    break
                if i[j] == i[k]:
                    i[j] += i[k]
                    i[k] = 0
                    break
    # 왼쪽으로 밀기
    for i in range(n):
        q = []
        for j in range(0, n):
            if board[i][j] != 0:
                q.append(board[i][j])
                board[i][j] = 0

        for j in range(0, n):
            if len(q) != 0:
                board[i][j] = q.pop(0)
            else:
                break
    # 오른쪽
    for i in range(n):
        board[i].reverse()

def up(board):
    # reverse
    temp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][i] = board[i][j]


    for i in temp:
        for j in range(0, len(i)-1): #0,1 / 2 2 2
            for k in range(j+1, n):
                if i[j] == 0:
                    break
                if i[j] != i[k] and i[k] != 0:
                    break
                if i[j] == i[k]:
                    i[j] += i[k]
                    i[k] = 0
                    break
    # 왼쪽으로 밀기
    for i in range(n):
        q = []
        for j in range(0, n):
            if temp[i][j] != 0:
                q.append(temp[i][j])
                temp[i][j] = 0

        for j in range(0, n):
            if len(q) != 0:
                temp[i][j] = q.pop(0)
            else:
                break
    # reverse
    for i in range(n):
        for j in range(n):
            board[j][i] = temp[i][j]
def down(board):
    # reverse
    temp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][i] = board[i][j]
    # reverse
    for i in range(n):
        temp[i].reverse()

    for i in temp:
        for j in range(0, len(i)-1): #0,1 / 2 2 2
            for k in range(j+1, n):
                if i[j] == 0:
                    break
                if i[j] != i[k] and i[k] != 0:
                    break
                if i[j] == i[k]:
                    i[j] += i[k]
                    i[k] = 0
                    break
    # 왼쪽으로 밀기
    for i in range(n):
        q = []
        for j in range(0, n):
            if temp[i][j] != 0:
                q.append(temp[i][j])
                temp[i][j] = 0

        for j in range(0, n):
            if len(q) != 0:
                temp[i][j] = q.pop(0)
            else:
                break

    # reverse
    for i in range(n):
        temp[i].reverse()
    # reverse
    for i in range(n):
        for j in range(n):
            board[j][i] = temp[i][j]

# right(board)
# for i in board:
#     print(i)
# print()
# down(board)
# for i in board:
#     print(i)
# print()
# up(board)
# for i in board:
#     print(i)
# print()

maxs = 0
for i in check_list:
    temp_board = copy.deepcopy(board)
    for j in i:
        if j==0:
            left(temp_board)
        elif j==1:
            right(temp_board)
        elif j==2:
            up(temp_board)
        elif j==3:
            down(temp_board)
    # print(temp_board)
    for j in temp_board:
        if max(j) > maxs:
            maxs = max(j)
            # print("--------------------------")
print(maxs)

