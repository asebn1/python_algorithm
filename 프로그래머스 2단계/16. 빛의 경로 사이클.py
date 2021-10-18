from collections import defaultdict


def solution(grid):
    answer = []
    grid = list(map(lambda x: list(x), grid))
    n, m = len(grid), len(grid[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dic = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in d:
                if k not in dic[(i, j)]:
                    d1, d2 = k
                    x, y = i, j
                    result = 0

                    while (d1, d2) not in dic[(x, y)]:
                        result += 1
                        dic[(x, y)].append((d1, d2))
                        x += d1
                        y += d2

                        if x == -1: x = n - 1
                        if x == n: x = 0
                        if y == -1: y = m - 1
                        if y == m: y = 0

                        s = grid[x][y]

                        if s == 'L': d1, d2 = (d2, d1) if d1 != 0 else (-d2, -d1)
                        if s == 'R': d1, d2 = (-d2, -d1) if d1 != 0 else (d2, d1)

                    answer.append(result)

    answer.sort()

    return answer


print(solution(['SL', 'LR']))  # [16]