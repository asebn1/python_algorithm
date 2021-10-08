# 재귀
def solv(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0

    return solv(numbers[1:], target + numbers[0]) + solv(numbers[1:], target - numbers[0])


def solution(numbers, target):
    return solv(numbers, target)