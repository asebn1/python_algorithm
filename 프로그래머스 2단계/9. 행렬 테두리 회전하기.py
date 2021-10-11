import copy


def solution(rows, columns, queries):
    answer = []
    cnt = 1
    base = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            base[i][j] = cnt
            cnt += 1

    for i in queries:
        # 새로 만든 보드
        board_x, board_y = abs(i[0] - i[2]) + 1, abs(i[1] - i[3]) + 1
        board = [[0] * board_y for _ in range(board_x)]
        # 복사할 위치
        minx, miny = min(i[0], i[2]) - 1, min(i[1], i[3]) - 1
        # 보드에 복사
        for cx in range(board_x):
            for cy in range(board_y):
                board[cx][cy] = base[cx + minx][cy + miny]
        list_check = []
        # 1
        for i in range(0, board_y):
            list_check.append((0, i))
        # 2
        for i in range(1, board_x):
            list_check.append((i, board_y - 1))
        # 3
        for i in range(board_y - 2, -1, -1):
            list_check.append((board_x - 1, i))
        # 4
        for i in range(board_x - 2, -1, -1):
            list_check.append((i, 0))
        # 복사용
        new_board = copy.deepcopy(board)
        change = []
        for i in range(0, len(list_check) - 1):
            # 바꾸기
            cx, cy = list_check[i]
            nx, ny = list_check[i + 1]
            board[nx][ny] = new_board[cx][cy]
            change.append(new_board[cx][cy])
        # board를 base에 넣기
        for cx in range(board_x):
            for cy in range(board_y):
                base[cx + minx][cy + miny] = board[cx][cy]
        answer.append(min(change))

    return answer


""" (0,0) 
    (3,2)
0,0 -> 0,1
0,1 -> 0,2

0,2 -> 1,2 / 0,3
1,2 -> 2,2
2,2 -> 3,2

3,2 -> 3,1
3,1 -> 3,0

3,0 -> 2,0
2,0 -> 1,0
1,0 -> 0,0






"""