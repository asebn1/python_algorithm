from itertools import combinations
import copy
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arrow_list = []
for i in range(m):
    arrow_list.append((n, i))
combi = list(combinations(arrow_list, 3))

def check(chcek_board): # 1이 없을때까지
    for i in chcek_board:
        if i.count(1) > 0:
            return True
    return False
maxs = 0
for com in combi:
    ret = 0
    temp_board = copy.deepcopy(board)
    while check(temp_board):
        # 쏠것 확인
        kill_list = []
        for arrow in com: # 3개
            in_list = []  # 조건 안, 거리, 위치
            for i in range(n):
                for j in range(m):
                    if temp_board[i][j] != 1:
                        continue
                    if (abs(arrow[0]-i)+abs(arrow[1]-j)) <= d:
                        in_list.append(((abs(arrow[0]-i)+abs(arrow[1]-j)), i, j))
            # 추가
            if len(in_list) > 0:
                in_list = sorted(in_list, key = lambda x : (x[0], x[2]))
                kill_list.append((in_list[0][1], in_list[0][2]))
        # 없애기
        kill_list = list(set(kill_list))
        ret += len(kill_list)

        if len(kill_list) > 0:
            for i in kill_list:
                temp_board[i[0]][i[1]] = 0
        # 전진
        temp_board = [[0]*m] + temp_board
        temp_board = temp_board[:-1]
    if maxs < ret:
        maxs = ret
print(maxs)
