import copy
def solution(name):
    board = list(name)
    print(board)
    non_check = []
    n = len(name)
    for i in range(n):
        temp = []
        count = -1
        for j in range(i, n):
            count += 1
            temp.append(count)
        for j in range(0, i):
            count -= 1
            temp.append(count)
        non_check.append(temp)
    # A체크
    # n = 10이면, A_NON_CHECK = 10
    a_non_check = n
    for i in non_check:
        test = copy.deepcopy(board)
        n_cnt = -1
        for j in i:
            test[j] = 'A'
            n_cnt+=1
            if test.count('A') == n:
                if n_cnt < a_non_check:
                    a_non_check = n_cnt
                break
    alpha = []
    for i in range(ord('A'),ord('Z')+1):
        alpha.append(chr(i))
    current = 0
    result = 0
    for i in board:
        if i == 'A':
            continue
        c1, c2 = 0,0
        cnt1, cnt2 = 0,0
        # 앞으로
        while 1:
            if c1 >= len(alpha):
                c1 = 0
            if alpha[c1]==i:
                break
            else:
                c1 += 1
                cnt1 += 1
        while 1:
            if c2 < 0:
                c2 = len(alpha)-1
            if alpha[c2]==i:
                break
            else:
                c2 -= 1
                cnt2 += 1
        current = alpha.index(i)
        print(cnt1, cnt2)
        result += min(cnt1, cnt2)
    print(result, a_non_check)
    result += a_non_check
    print("---")
    return result
print(solution("JAZ"))