from itertools import combinations


def solution(relation):
    # 6 세로
    min = len(relation)
    # 4 가로
    x = len(relation[0])

    # [0, 1, 2, 3, (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    arr = []

    # 0, 1, 2, 3
    temp = []
    for i in range(x):
        temp.append(i)
        arr.append(i)

    # 순열
    for i in range(2, x + 1):
        for j in list(combinations(temp, i)):
            arr.append(j)

    # 0, [1, 2] 되도록 저장하는 곳
    group = []

    # 1개씩
    for i in range(x):
        temp = set()
        for j in range(min):
            temp.add(relation[j][i])
        if min == len(temp):
            group.append(i)

    # 최소성 삭제 1
    # [0, 1, 2, 3, (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    for i in range(x):
        arr.remove(i)

    # [1, 2, 3]
    for i in arr:
        y = True
        # group 겹치는 것 넘기기
        for g in group:
            if str(type(g)) == "<class 'int'>":
                if g in i:
                    y = False
            elif str(type(g)) == "<class 'tuple'>":
                # 1, 2, 3
                cnt = 0
                for m in g:
                    if m in i:
                        cnt += 1
                if cnt == len(g):
                    y = False
        if y == False:
            continue

        temp = []
        # 0~5
        if str(type(i)) == "<class 'tuple'>":
            for k in range(min):
                # 1, 2, 3
                b = []
                for j in i:
                    b.append(relation[k][j])
                b = tuple(b)
                temp.append(b)
            temp = set(temp)
            if len(temp) == min:
                group.append(i)
    print(group)
    answer = len(group)
    return answer