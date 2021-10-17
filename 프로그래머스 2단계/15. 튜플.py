def solution(s):
    db = {}
    board = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    board = s.split(',')
    for i in board:
        if int(i) not in db.keys():
            db[int(i)] = 1
        else:
            db[int(i)] += 1
    db = sorted(db.items(), key=lambda x: -x[1])
    print(db)
    result = []
    for i in db:
        result.append(i[0])
    return result


"""
튜플
1. 중복가능
2. 순서
3. 원소 유한
"""