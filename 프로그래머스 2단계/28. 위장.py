from itertools import product, combinations
def solution(clothes):
    # 1. db로 저장
    db = {}
    for i in clothes:
        if i[1] not in db.keys():
            db[i[1]] = 1
        else:
            db[i[1]] += 1
    cnt = 1
    for i in db.values():
        cnt *= (i+1)
    return cnt-1