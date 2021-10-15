def check(places):
    # 2차원 배열
    board = []
    for i in places:
        board.append(list(i))
    # print(board)

    # 오/아래
    dx = [0, 1]
    dy = [1, 0]
    # 1. 오/아래
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'P':
                continue
            for idx in range(2):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if not (0 <= nx <= 4 and 0 <= ny <= 4):
                    continue
                if board[nx][ny] == 'P':
                    return 0

    # 2. 대각선 왼오
    dx = [1, 1]
    dy = [-1, 1]
    # 0,0 / 1,-1 / -> 0,-1  [i][ny]/ 1,0 [nx][j]
    # 0,0 / 1,1 / 0,1 [i][ny] / 1,0 [nx][j]
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'P':
                continue
            for idx in range(2):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if not (0 <= nx <= 4 and 0 <= ny <= 4):
                    continue
                if board[nx][ny] == 'P':
                    if board[i][ny] == 'X' and board[nx][j] == 'X':
                        continue
                    else:
                        return 0
    # 3. POP
    # 0,0 / O,2 -> 0,1
    # 0,0 / 2,0 -> 1,0
    # 1. 오/아래

    dx = [0, 2]
    dy = [2, 0]
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'P':
                continue
            for idx in range(2):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if not (0 <= nx <= 4 and 0 <= ny <= 4):
                    continue
                # 0,2
                if idx == 0:
                    if board[nx][ny] == 'P' and board[nx][ny - 1] == 'O':
                        return 0
                # 2,0
                if idx == 1:
                    if board[nx][ny] == 'P' and board[nx - 1][ny] == 'O':
                        return 0
    return 1


def solution(places):
    result = []
    for i in range(5):
        result.append(check(places[i]))
    return result