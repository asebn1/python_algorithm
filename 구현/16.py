import copy
n, m, h = map(int, input().split())
board = [[0]*(n-1) for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
# for i in board:
#     print(i)

idx_list = [i for i in range(1, n+1)]
# print(idx_list)
# idx 체크

# 진짜인지
def check(temp_board):
    cnt = 0
    for i in idx_list: # 1,2,3,4,5
        real_idx=i
        idx = i
        for j in range(h): # 높이만큼 0~5
            if idx==1:
                if temp_board[j][0]==1:
                    idx+=1
            elif idx==n:
                if temp_board[j][idx-2]==1:
                    idx-=1
            else:
                if temp_board[j][idx-2] == 1:
                    idx -= 1
                elif temp_board[j][idx-1] == 1:
                    idx += 1
        if real_idx == idx:
            cnt += 1
        else:
            break
    if cnt == n:
        return True
    else:
        return False
if check(board):
    print(0)
else:
    # permu
    permu = []
    first = []
    for i in range(h):
        for j in range(n-1):
            if board[i][j] == 0:
                first.append((i,j))
    # dfs 2개
    s = []
    def dfs2():
        if len(s) == 2:
            permu.append(s.copy())
            return
        for i in range(0, len(first)):
            if first[i] in s:
                continue
            s.append(first[i])
            dfs2()
            s.pop()
    def dfs3():
        if len(s) == 3:
            permu.append(s.copy())
            return
        for i in range(0, len(first)):
            if first[i] in s:
                continue
            s.append(first[i])
            dfs3()
            s.pop()
    dfs2()
    dfs3()
    temp_list = []
    for i in first:
        temp_list.append([i])

    permu = temp_list + permu
    # 체크
    booli = False
    for i in permu:
        temp_board = copy.deepcopy(board)
        for j in i:
            # print(j)
            x, y = j[0], j[1]
            temp_board[x][y] = 1
        if check(temp_board):
            booli = True
            print(len(i))
            break
    if booli == False:
        print(-1)
