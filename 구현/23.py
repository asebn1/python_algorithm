import copy
from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

virus_list = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_list.append((i, j))
# print(virus_list)
combi = []
s = []
def dfs(start):
    if len(s) == m:
        combi.append(s.copy())
        return
    for i in range(start, len(virus_list)):
        if i in s:
            continue
        if len(s)>0 and s[-1] > i:
            continue
        s.append(i)
        dfs(start+1)
        s.pop()
dfs(0) # 조합 리스트
# 값으로 저장
combination = []
for i in combi:
    temp = []
    for j in i: # 0,1,2
        temp.append(virus_list[j])
    combination.append(temp)

# print(combination)

# 바이러스가 전파 성공? -> 성공하면 True
def checkVirus(board):
    for i in board:
        if 0 in i:
            return False
    return True
# print(checkVirus())
# bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ret = 10000
def bfs():
    global board, ret
    for i in combination:
        temp_board = copy.deepcopy(board)
        q = deque()
        for j in i:
            x, y = j
            # q에 저장
            q.append((0, x, y))

        # visited
        visited = [[False]*n for _ in range(n)]
        while q:
            dist, x, y = q.popleft()
            visited[x][y] = True
            if ret < dist:
                break
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 예외상황
                if not (0 <= nx < n and 0 <= ny < n): #범위
                    continue
                if board[nx][ny] == 1: # 벽
                    continue
                if visited[nx][ny] == True: #방문했던곳
                    continue
                q.append((dist+1, nx, ny))
                visited[nx][ny] = True
                temp_board[nx][ny] = 2

            if checkVirus(temp_board) and ret > dist+1:
                ret = dist + 1
                break

if checkVirus(board):
    print(0)
else:
    bfs()
    if ret == 10000:
        print(-1)
    else:
        print(ret)