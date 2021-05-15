n, m = map(int, input().split())
x,y,d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
# 방향 설정
if d == 1:
    d = 3
elif d == 3:
    d = 1
# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = []
q.append((x,y,d))
while q:
    # x, y, dx 0~3
    x1, y1, d1 = q.pop(0)
    # 현재 있는 곳 청소
    board[x1][y1] = 2
    temp = d1
    check = False
    for i in range(temp+1, temp+5): # 2, 2345
        temp_i = i
        if temp_i >= 4:
            temp_i -= 4
        # print(temp_i)
        nx = x1 + dx[temp_i]
        ny = y1 + dy[temp_i]
        if board[nx][ny] == 0:
            q.append((nx, ny, temp_i))
            check = True
            break
    # 4방향중 0이 있기때문에 continue
    if check==True:
        continue
    # 4방향 모두 0이 아니면,
    nx = x1 - dx[d1]
    ny = y1 - dy[d1]
    # 벽이 아니면 이동
    if board[nx][ny] != 1:
        q.append((nx, ny, d1))
result = 0
for i in board:
    result += i.count(2)
print(result)


