n,m,h = map(int, input().split())
board = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
ans = 4 # 결과값

# 옳은 사다리인지
def check():
    for start in range(n):
        k = start
        for j in range(h):
            if board[j][k]: # 가로선
                k += 1
            elif k > 0 and board[j][k-1]: # 왼쪽선
                k -= 1
        if k != start:
            return False
    return True
# dfs
def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or ans <= cnt:
        return
    for i in range(x, h):
        # 행 변경시
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if not board[i][j] and not board[i][j+1]: # 오른쪽
                if j>0 and board[i][j-1]: # 왼쪽
                    continue
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0
dfs(0,0,0)
if ans > 3:
    print(-1)
else:
    print(ans)
