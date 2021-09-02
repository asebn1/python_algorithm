from collections import deque


def solution(n, results):
    win_board = [[] for _ in range(n + 1)]
    lost_board = [[] for _ in range(n + 1)]
    for i in results:
        win = i[0]
        lost = i[1]
        win_board[lost].append(win)
        lost_board[win].append(lost)

    def solv(num):
        visited = [False] * (n + 1)
        q = deque()
        total_board = set()
        q.append(num)
        # win
        while q:
            pop = q.popleft()  # 4 3 1
            for i in win_board[pop]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    total_board.add(i)
        # lost
        q.append(num)
        while q:
            pop = q.popleft()  # 4 3 1
            for i in lost_board[pop]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    total_board.add(i)
        print(num, total_board)
        if len(list(total_board)) == n - 1:
            return 1

    print(win_board)
    print(lost_board)
    answer = 0
    for i in range(1, n + 1):
        if solv(i):
            answer += 1
    return answer