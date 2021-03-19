def solution(n):
    board = [0] * 10001
    for i in range(1, 10001):
        board[i] = i
    cnt = 0
    for i in range(1, len(board)):
        check = 0
        for j in range(i, len(board)):
            if sum(board[i:j]) >= n:
                check = sum(board[i:j])
                break
        if check == n:
            cnt += 1
    return cnt