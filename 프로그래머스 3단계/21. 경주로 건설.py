from collections import deque


def solution(board):
    def bfs(start):
        INF = int(1e9)
        n = len(board)
        table = [[INF] * n for _ in range(n)]
        # 상 하 좌 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append(start)
        while q:
            x, y, dist, head = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 넘어가면
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if board[nx][ny] == 1:
                    continue
                n_cost = 0
                if i != head:
                    n_cost += 600
                else:
                    n_cost += 100
                if table[nx][ny] > n_cost + dist:
                    table[nx][ny] = n_cost + dist
                    q.append((nx, ny, dist + n_cost, i))
        return table[-1][-1]

    return min(bfs((0, 0, 0, 1)), bfs((0, 0, 0, 3)))
    # for i in table:
    #     print(i)