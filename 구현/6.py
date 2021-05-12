n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

maxs = 0
# 1-1. 막대기 가로
for i in range(n):
    temp_max = 0
    for j in range(3, m):
        temp_max = sum(board[i][j-3:j+1])
        if maxs < temp_max:
            maxs = temp_max

# 1-2. 막대기 세로
for i in range(m):
    for j in range(3, n): # 5
        temp_max = 0
        for k in range(j-3, j+1): #0 3
            temp_max += board[k][i]
        if maxs < temp_max:
            maxs = temp_max

# 2. 정사각형
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+1<n and 0<=j+1<m):
            continue
        temp_max = board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1]
        if maxs < temp_max:
            maxs = temp_max

# 3-1. L자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+2<n and 0<=j+1<m):
            continue
        temp_max1 = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1] # L
        temp_max2 = board[i][j+1] + board[i+1][j+1] + board[i+2][j] + board[i+2][j+1]
        temp_max3 = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
        temp_max4 = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]

        if maxs < max(temp_max1, temp_max2, temp_max3, temp_max4):
            maxs = max(temp_max1, temp_max2, temp_max3, temp_max4)
# 3-2 ㄱ자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+1<n and 0<=j+2<m):
            continue
        temp_max1 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
        temp_max2 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
        temp_max3 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        temp_max4 = board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]

        if maxs < max(temp_max1, temp_max2, temp_max3, temp_max4):
            maxs = max(temp_max1, temp_max2, temp_max3, temp_max4)

# 4-1. 용1자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+2<n and 0<=j+1<m):
            continue
        temp_max1 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        temp_max2 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]

        if maxs < max(temp_max1, temp_max2):
            maxs = max(temp_max1, temp_max2)

# 4-2. 용ㅡ자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+1<n and 0<=j+2<m):
            continue
        temp_max1 = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
        temp_max2 = board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1]

        if maxs < max(temp_max1, temp_max2):
            maxs = max(temp_max1, temp_max2)

# 5-1. ㅏ자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+2<n and 0<=j+1<m):
            continue
        temp_max1 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
        temp_max2 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        if maxs < max(temp_max1, temp_max2):
            maxs = max(temp_max1, temp_max2)

# 5-2. ㅗ자
for i in range(n):
    for j in range(m):
        temp_max = 0
        if not (0<=i+1<n and 0<=j+2<m):
            continue
        temp_max1 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        temp_max2 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]

        if maxs < max(temp_max1, temp_max2):
            maxs = max(temp_max1, temp_max2)
print(maxs)
"""
1. 겹침 X
2. 도형은 모두 연결
3. 변끼리 연결

N*M

"""