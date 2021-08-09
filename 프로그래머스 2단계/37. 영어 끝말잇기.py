def solution(n, words):
    db = [[] for _ in range(n + 1)]
    last = words[0][0]
    idx = 1
    talked = []
    for i in words:
        if idx == n + 1:
            idx = 1
        # 끝말잇기 성공
        if i[0] == last:
            # 말했던적 있음
            if i in talked:
                return [idx, len(db[idx]) + 1]
            else:
                db[idx].append(i)
                talked.append(i)
        # 실패
        else:
            return [idx, len(db[idx]) + 1]
        last = i[-1]
        idx += 1

    return [0, 0]


"""
1~N->1 끝말잇기


"""