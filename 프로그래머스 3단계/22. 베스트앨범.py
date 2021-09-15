def solution(genres, plays):
    db = {}
    db_sq = {}
    n = len(genres)
    genre_list = list(set(genres))

    for i in range(n):
        if genres[i] not in db.keys():
            db[genres[i]] = [(plays[i], i)]
            db_sq[genres[i]] = plays[i]
        else:
            # if len(db[genres[i]]) < 2:
            db[genres[i]].append((plays[i], i))
            db_sq[genres[i]] += plays[i]
    # 정렬
    for i in genre_list:
        db[i] = sorted(db[i], key=lambda x: (x[0], -x[1]))
    print(db)
    db_sq = sorted(db_sq.items(), key=lambda x: -x[1])

    # print(db)
    # print(db_sq)
    # 결과
    result = []
    for i in db_sq:
        name, cost = i
        # print(name, cost)
        cnt = 0
        while 1:
            if len(db[name]) != 0:
                cost, idx = db[name].pop()
                result.append(idx)
                cnt += 1
            if len(db[name]) == 0:
                break
            if cnt == 2:
                break
    return result


print(solution(['A', 'B', 'A'], [600, 500, 600]))  # == [0, 2, 1])
# print(solution(['A', 'B', 'A'], [600, 500, 700]) == [2, 0, 1])
# print(solution(['A', 'A', 'A'], [600, 500, 700]) == [2, 0])
# print(solution(['A', 'A', 'A'], [3, 2, 1]) == [0, 1])
# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
# print(solution(['classic'], [2500]) == [0])
# print(solution(['A', 'B', 'C'], [1, 2, 3]) == [2, 1, 0])
# print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]) == [2, 1, 0, 3])
# print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) == [3, 0, 2])
# print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) == [0, 1, 2])
# print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])

"""
가장 많이 재생된 노래 2개씩 그룹
노래 : 고유번호
1. 장르 
2. 노래
3. 고유번호 순
"""