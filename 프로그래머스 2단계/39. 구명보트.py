from collections import deque


def solution(people, limit):
    board = deque(sorted(people, reverse=True))

    cnt = 0
    while 1:
        # 0, 1
        if len(board) == 0:
            break
        elif len(board) == 1:
            board.popleft()
            cnt += 1
            break
        # 2개 이상
        if len(board) >= 2 and board[0] + board[-1] <= limit:
            board.popleft()
            board.pop()
            cnt += 1
        else:
            board.popleft()
            cnt += 1

    return cnt


"""
최대 2명
무게제한 100
70 50 80 50 -> (1,2) (2,3) (3,4)

"""