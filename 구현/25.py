n, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
chase_board = [[[]*n for _ in range(n)] for _ in range(n)]
chase_idx = []
for i in range(k):
    x, y, d = map(int, input().split())
    chase_idx.append(d-1)
    chase_board[x-1][y-1].append(i+1)
# 이동 1번부터
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# print(chase_idx)
ret = 0
check = False
while 1:
    ret += 1
    for i in range(k):
        d = chase_idx[i]
        x, y = -1, -1
        # x, y 찾기
        for t1 in range(n):
            for t2 in range(n):
                if (i+1) in chase_board[t1][t2]:
                    x = t1
                    y = t2
                    break
        # 범위 넘어감 or 파란색 타일
        # d를 반대로
        if (not (0 <= (x + dx[d]) < n and  0<= (y+dy[d]) <n)) or board[(x + dx[d])][(y+dy[d])]==2:
            if d==0:
                d = 1
            elif d== 1:
                d = 0
            elif d== 2:
                d = 3
            elif d== 3:
                d = 2
        nx = x + dx[d]
        ny = y + dy[d]
        # 반대로 범위 넘어가거나 파란색일때 가만히
        if (not (0 <= nx < n and  0<= ny <n)) or board[nx][ny]==2:
            chase_idx[i] = d
            continue
        # 흰색
        if board[nx][ny] == 0:
            # 전달할 리스트
            temp_list = chase_board[x][y][chase_board[x][y].index(i+1):]
            chase_board[x][y] = chase_board[x][y][:chase_board[x][y].index(i+1)]
            # 다음 리스트에 추가
            chase_board[nx][ny] += temp_list
            chase_idx[i] = d
            # print(temp_list)
        # 빨간색
        elif board[nx][ny] == 1:
            # 전달할 리스트
            temp_list = chase_board[x][y][chase_board[x][y].index(i+1):]
            chase_board[x][y] = chase_board[x][y][:chase_board[x][y].index(i+1)]
            # 반대로 변환
            temp_list = temp_list[::-1]
            # 다음 리스트에 추가
            chase_board[nx][ny] += temp_list
            chase_idx[i] = d
        for t1 in range(n):
            for t2 in range(n):
                if len(chase_board[t1][t2])>=4:
                    check = True
                    break
    if check == True:
        break
    if ret == 1001:
        break
if k == 1:
    print(0)
elif ret == 1001:
    print(-1)
else:
    print(ret)


# for i in chase_board:
#     print(i)
# print(chase_idx)