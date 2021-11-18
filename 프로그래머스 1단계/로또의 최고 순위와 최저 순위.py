def solution(lottos, win_nums):
    result = []
    zero_cnt = lottos.count(0)
    how_in = 0
    for i in lottos:
        if i in win_nums:
            how_in += 1
    max_in = zero_cnt + how_in
    if max_in >= 6:
        result.append(1)
    elif max_in >= 5:
        result.append(2)
    elif max_in >= 4:
        result.append(3)
    elif max_in >= 3:
        result.append(4)
    elif max_in >= 2:
        result.append(5)
    else:
        result.append(6)

    if how_in >= 6:
        result.append(1)
    elif how_in >= 5:
        result.append(2)
    elif how_in >= 4:
        result.append(3)
    elif how_in >= 3:
        result.append(4)
    elif how_in >= 2:
        result.append(5)
    else:
        result.append(6)

    return result