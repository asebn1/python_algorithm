from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 위치
x=0
y=1
ret = 0
def check(d, x, y):
    if d==1 or d==3:
        if not (0<=x<n and 0<=y<n):
            return False
        if board[x][y] == 1:
            return False
    else:
        if not (0<=x<n and 0<=y<n):
            return False
        if board[x][y] == 1 or board[x-1][y] == 1 or board[x][y-1] == 1:
            return False
    return True

def bfs():
    global x, y, ret
    q = deque()
    q.append((1, x, y))
    while q:
        d, nx, ny = q.popleft()
        if nx==n-1 and ny==n-1:
            ret += 1
            continue
        if d == 1:
            # 가로
            if check(1, nx, ny+1):
                q.append((1, nx, ny+1))
            # 대각선
            if check(2, nx+1, ny+1):
                q.append((2, nx+1, ny+1))
        elif d==2:
            # 가로
            if check(1, nx, ny+1):
                q.append((1, nx, ny+1))
            # 대각선
            if check(2, nx+1, ny+1):
                q.append((2, nx+1, ny+1))
            # 세로
            if check(3, nx+1, ny):
                q.append((3, nx+1, ny))
        else:
            # 대각선
            if check(2, nx+1, ny+1):
                q.append((2, nx+1, ny+1))
            # 세로
            if check(3, nx+1, ny):
                q.append((3, nx+1, ny))
bfs()
print(ret)