from collections import deque


def solution(priorities, location):
    db = []
    for i in range(0, len(priorities)):
        db.append((priorities[i], i))
    board = deque(sorted(priorities, reverse=True))
    selected = priorities[location]
    # 최대순서 board
    # db = (값, 인덱스)
    db = deque(db)

    cnt = 0
    while 1:
        # 맨앞 가장 큰 것 맞춰주기
        while 1:
            if board[0] != db[0][0]:
                temp = db.popleft()
                db.append(temp)
            else:
                break
        value, index = db.popleft()
        board.popleft()
        cnt += 1
        if index == location:
            break

    return cnt