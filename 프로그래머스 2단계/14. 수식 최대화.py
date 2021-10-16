from itertools import permutations
import copy
def solution(expression):
    checkList = list(permutations(['*','+','-'], 3))
    # 구간 배열로 나누기
    board = list(expression)
    result = []
    temp = ''
    for i in board:
        if ord('0') <= ord(i) <= ord('9'):
            temp += i
        else:
            result.append(int(temp))
            result.append(i)
            temp = ''
    result.append(int(temp))
    result_real = result
    # 6가지
    max_check = 0
    answer = []
    for i in checkList:
        result = copy.deepcopy(result_real)
        for j in i: #       * + -
            for r in range(len(result)):
                if result[r] == j:
                    if j=='*':
                        result[r+1] = result[r-1]*result[r+1]
                    elif j=='+':
                        result[r+1] = result[r-1]+result[r+1]
                    elif j=='-':
                        result[r+1] = result[r-1]-result[r+1]
                    result[r], result[r-1] = '', ''
            # print(result)
            while 1:
                if '' not in result:
                    break
                result.remove('')
        answer.append(result[0])
    for i in range(len(answer)):
        answer[i] = abs(answer[i])
    print(answer)
    return max(answer)