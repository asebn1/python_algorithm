from itertools import permutations
import math
def prime(x):
    if x <= 1:
        return 0
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return 0
    return 1

def solution(numbers):
    board = list(numbers)
    # 크기 n
    n = len(board)
    sample = []
    sample += board
    for i in range(2, n+1):
        sample += list(permutations(board,i))
    result = []
    for i in sample:
        result.append(int(''.join(i)))
    result = list(set(result))
    cnt=0
    print(result)
    for i in result:
        if prime(i):
            cnt+=1
    return cnt