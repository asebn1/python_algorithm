tot1 = list(map(int, input()))
tot2 = list(map(int, input()))
tot3 = list(map(int, input()))
tot4 = list(map(int, input()))

k = int(input())
board = []
for i in range(k):
    a, b = map(int, input().split())
    board.append((a, b))
# print(board)

def check(t1, t2):
    # 다르면 1
    if t1[2] != t2[6]:
        return 1
    # 같으면 0
    return 0
def trans(t1, d):
    if d == -1:
        t1[0], t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7] = t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7], t1[0]
    else:
        t1[0], t1[1], t1[2], t1[3], t1[4], t1[5], t1[6], t1[7] = t1[7], t1[0], t1[1], t1[2], t1[3], t1[4], t1[5], t1[6]

for i in board:
    idx, d = i
    if idx == 1:
        # 1-2번체크
        visit2 = False
        visit3 = False
        visit4 = False
        if check(tot1, tot2):
            visit2 = True
        if check(tot2, tot3):
            visit3 = True
        if check(tot3, tot4):
            visit4 = True
        # 1번 회전
        trans(tot1, d)
        # 2번
        if visit2 == True:
            d *= -1
            trans(tot2, d)
        else:
            continue
        # 3번
        if visit3 == True:
            d *= -1
            trans(tot3, d)
        else:
            continue
        # 4번
        if visit4 == True:
            d *= -1
            trans(tot4, d)
        else:
            continue
    if idx == 3:
        # 1,2,4번체크
        visit1 = False
        visit2 = False
        visit4 = False
        if check(tot1, tot2):
            visit1 = True
        if check(tot2, tot3):
            visit2 = True
        if check(tot3, tot4):
            visit4 = True
        # 1번 회전
        trans(tot3, d)
        if visit2 == True or visit4 == True:
            d *= -1
        else:
            continue
        # 2번
        if visit2 == True:
            trans(tot2, d)
        # 4번
        if visit4 == True:
            trans(tot4, d)
        if visit2 != True:
            continue
        # 1번
        if visit1 == True:
            d *= -1
            trans(tot1, d)
    if idx == 2:
        # 1,3,4번체크
        visit1 = False
        visit3 = False
        visit4 = False
        if check(tot1, tot2):
            visit1 = True
        if check(tot2, tot3):
            visit3 = True
        if check(tot3, tot4):
            visit4 = True
        # 2번 회전
        trans(tot2, d)
        if visit1 == True or visit3 == True:
            d *= -1
        else:
            continue
        # 1번
        if visit1 == True:
            trans(tot1, d)
        # 3번
        if visit3 == True:
            trans(tot3, d)

        if visit3 != True:
            continue
        # 4번
        if visit4 == True:
            d *= -1
            trans(tot4, d)
    if idx == 4:
        # 1-3번체크
        visit1 = False
        visit2 = False
        visit3 = False
        if check(tot1, tot2):
            visit1 = True
        if check(tot2, tot3):
            visit2 = True
        if check(tot3, tot4):
            visit3 = True
        # 4번 회전
        trans(tot4, d)
        # 3번
        if visit3 == True:
            d *= -1
            trans(tot3, d)
        else:
            continue
        # 2번
        if visit2 == True:
            d *= -1
            trans(tot2, d)
        else:
            continue
        # 4번
        if visit1 == True:
            d *= -1
            trans(tot1, d)
        else:
            continue
answer = tot1[0]*1 + tot2[0]*2 + tot3[0]*4 + tot4[0]*8
print(answer)




















