N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]  # Board
dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
queue = []  # BFS : queue 활용
# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]


rx, ry, bx, by = 0, 0, 0, 0  # 초기화
for i in range(N):
    for j in range(M):
        if B[i][j] == 'R':
            rx, ry = i, j
        elif B[i][j] == 'B':
            bx, by = i, j
# 위치 정보와 depth(breadth 끝나면 +1)
queue.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True