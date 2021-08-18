from itertools import combinations


result_dist = int(1e9)
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 치킨집 위치 저장, 집 위치 저장
chicken_locate = []
home_locate = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken_locate.append([i, j])
        if board[i][j] == 1:
            home_locate.append([i, j])


# 각 치킨 m개 조합
chicken_combi = list(combinations(chicken_locate, m))

# 각 집에서 치킨집까지 거리 계산

    # 모든 조합
for combi in chicken_combi:
    total_check = 0
    for home_r, home_c in home_locate:
        # 해당 집에서 가장 가까운 치킨집 1개
        min_check = int(1e9)
        for r, c in combi:
            check = abs(home_r-r) + abs(home_c-c)
            if check < min_check:
                min_check = check
        total_check += min_check
    if total_check < result_dist:
        result_dist = total_check
# 도시의 치킨 거리의 최소 값
print(result_dist)