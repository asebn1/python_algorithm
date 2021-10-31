def solution(board):
    n, m = len(board), len(board[0])
    # 현재, 오른쪽, 아래 값 같고, 0이 아니면 대각선값은 현재값+1
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    m = 0
    for i in board:
        m = max(m, max(i))
    return m * m


print(solution([[1]]))