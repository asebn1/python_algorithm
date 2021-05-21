import copy
n = int(input())
people_db = []
board = [[0]*n for _ in range(n)]
for i in range(n):
    people_db.append(list(map(int, input().split())))
# d1 <- 왼쪽
dist = []
for i in range(1, n):
    dist.append(i)
permu = []
s = []
def dfs():
    if len(s) == 2:
        permu.append(s.copy())
        return
    for i in range(0, len(dist)):
        s.append(dist[i])
        dfs()
        s.pop()
dfs()
permutation = []
for i in permu:
    if sum(i) > n:
        continue
    permutation.append(i)
# print(permutation)
d1, d2 = 1, 1
def makeBoard(board, x, y, d1, d2):
    temp_y = y
    for i in range(x, x+d1+1):
        if not (0<=i<n and 0<= temp_y < n):
            return False
        board[i][temp_y] = 5
        temp_y-=1
    # 오른쪽
    temp_y = y
    next_x, next_y = 0, 0
    for i in range(x+1, x+d2+1):
        temp_y+=1
        if not (0<=i<n and 0<= temp_y < n):
            return False
        board[i][temp_y] = 5
        next_x = i
        next_y = temp_y
    # 오른쪽 아래
    nn_x, nn_y = 0, 0
    for i in range(next_x+1, next_x+d1+1):
        if not (0<=i<n and 0<= next_y < n):
            return False
        next_y-=1
        board[i][next_y] = 5
        nn_x = i
        nn_y = next_y
    for i in range(nn_x-1, nn_x-d2-1, -1):
        if not (0<=i<n and 0<= nn_y < n):
            return False
        nn_y -= 1
        board[i][nn_y] = 5

    for i in range(len(board)):
        if board[i].count(5) == 2:
            cnt = 0
            for j in range(len(board[i])):
                if cnt == 2:
                    break
                if board[i][j] == 5:
                    cnt += 1
                    continue
                elif cnt == 1:
                    board[i][j] = 5
    # 1번 채우기
    if y+1 > n:
        return False
    for i in range(0, x+d1):
        for j in range(0, y+1):
            if board[i][j] == 0:
                board[i][j] = 1
    # 2번 채우기
    if x+d2+1 > n:
        return False
    for i in range(0, x+d2+1):
        for j in range(y, n):
            if board[i][j] == 0:
                board[i][j] = 2
    # 3번 채우기
    for i in range(x+d1, n):
        for j in range(0, y-d1+d2):
            if board[i][j] == 0:
                board[i][j] = 3
    # 4번 채우기
    for i in range(x+d2, n):
        for j in range(y-d1+d2, n):
            if board[i][j] == 0:
                board[i][j] = 4
    return True
# 인구 차이 확인
def distance(board):
    count = [0]*5
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count[0] += people_db[i][j]
            elif board[i][j] == 2:
                count[1] += people_db[i][j]
            elif board[i][j] == 3:
                count[2] += people_db[i][j]
            elif board[i][j] == 4:
                count[3] += people_db[i][j]
            elif board[i][j] == 5:
                count[4] += people_db[i][j]
    return max(count)-min(count)
# print(distance(board))
ret = int(1e9)
for i in range(n):
    for j in range(n):
        for p in permutation:
            d1, d2 = p
            if i+d1+d2 > n:
                continue
            if not (0 <= j-d1 < n and j+d2 < n):
                continue
            # print("dd")
            temp_board = copy.deepcopy(board)
            if makeBoard(temp_board, i, j, d1, d2):
                # for t in temp_board:
                    # print(t)
                if distance(temp_board) < ret:
                    ret = distance(temp_board)
print(ret)

