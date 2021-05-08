from collections import deque

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    board.append(list(input()))

rx, ry, bx, by = 0,0,0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            board[i][j] = '.'
            rx, ry = i, j
        if board[i][j] == 'B':
            board[i][j] = '.'
            bx, by = i, j

def move(rx,ry,dx,dy):
    count = 0
    x, y = rx, ry
    while 1:
        if board[x+dx][y+dy] == 'O':
            x += dx
            y += dy
            count += 1
            break
        if board[x+dx][y+dy] == '#':
            break
        x += dx
        y += dy
        count += 1
    return x,y,count

def bfs():
    global rx, ry, bx, by
    visited = []
    q = deque()
    q.append((rx,ry,bx,by,1))
    visited.append((rx,ry,bx,by))
    while q:
        rx,ry,bx,by,dist = q.popleft()
        for i in range(4):
            next_rx, next_ry, rcount = move(rx,ry,dx[i],dy[i])
            next_bx, next_by, bcount = move(bx,by,dx[i],dy[i])
            # B가 O에 도착
            if board[next_bx][next_by] == 'O':
                continue
            # R이 0에 도착
            if board[next_rx][next_ry] == 'O':
                if dist>10:
                    print(-1)
                else:
                    print(dist)
                return
            # print(next_rx, next_ry, rcount)
            # print(next_bx, next_by, bcount)
            ## 위치 같을 때
            if next_rx==next_bx and next_by==next_ry:
                if rcount > bcount:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.append((next_rx, next_ry, next_bx, next_by))
                q.append((next_rx, next_ry, next_bx, next_by, dist+1))
    print(-1)

bfs()