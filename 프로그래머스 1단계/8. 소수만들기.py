from itertools import combinations
import math


def prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    board = list(combinations(nums, 3))
    answer = 0
    for i in board:
        if prime_number(sum(i)):
            answer += 1

    return answer