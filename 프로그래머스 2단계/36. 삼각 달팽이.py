def solution(n):
    #
    board = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        board[i] = [0] * i

    total = 1
    for i in range(2, n + 1):
        total += i
    cnt = 0
    down_idx = n
    while 1:
        # 1. 위에서 밑으로 쭉 채우기
        for i in board:
            if 0 not in i:
                continue
            for j in range(0, len(i)):
                if i[j] == 0:
                    cnt += 1
                    i[j] = cnt
                    break

        # 2. 왼 -> 오른쪽으로 채우기
        if down_idx >= 1:
            for i in range(0, down_idx):
                if board[down_idx][i] != 0:
                    continue
                cnt += 1
                board[down_idx][i] = cnt
            down_idx -= 1
        # # 3. 위로 올리기
        for i in range(n, 0, -1):
            if 0 not in board[i]:
                continue
            for j in range(len(board[i]) - 1, -1, -1):
                if board[i][j] == 0:
                    cnt += 1
                    board[i][j] = cnt
                    break
        if cnt >= total:
            break
    answer = []
    for i in board:
        if len(i) >= 1:
            answer += i
    return answer