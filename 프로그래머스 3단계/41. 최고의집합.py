from itertools import product


def solution(n, s):
    mok = s // n
    na = s % n
    if mok == 0:
        return [-1]

    result = [mok] * n
    for i in range(na):
        result[i] += 1
    result.sort()
    return result