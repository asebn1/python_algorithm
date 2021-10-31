def solution(brown, yellow):
    hap = brown + yellow
    # 약수 구하기
    arr = []
    for i in range(1, int(hap / 2) + 1):
        if hap % i == 0:
            arr.append((i, int(hap / i)))
    result = []
    for i in arr:
        x, y = i[0] - 2, i[1] - 2
        if x < 1 or y < 1:
            continue
        check_hap = i[0] * 2 + i[1] * 2 - 4
        check_yellow = x * y

        if brown == check_hap and yellow == check_yellow:
            if i[0] > i[1]:
                return [i[0], i[1]]
            else:
                return [i[1], i[0]]