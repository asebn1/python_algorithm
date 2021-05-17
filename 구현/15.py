n = int(input())
board = [[0]*101 for _ in range(101)]
input_list = []
for i in range(n):
    input_list.append(list(map(int, input().split())))

# 우 상 좌 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
curve_list = []
for i in input_list:
    a,b,c,d = i
    curve = [c]
    for j in range(d):
        temp = curve[::-1]
        for i in range(len(temp)):
            temp[i] = (temp[i]+1) % 4
        curve = curve+temp
    curve_list.append(curve)

# 값 넣기
for i in range(n):
    x, y, t1, t2 = input_list[i]
    board[y][x] = 1 # y가 세로, x가 가로
    for j in curve_list[i]: # 0, 1
        ny = y + dy[j]
        nx = x + dx[j]
        if not (0<=nx<=100 and 0<=ny<=100):
            continue
        y = ny
        x = nx
        board[y][x] = 1
# 체크
ret = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
            ret += 1
print(ret)