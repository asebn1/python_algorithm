import math
def solution(arr):
    a = 0
    b = 0
    while 1:
        if len(arr) < 2:
            break
        a = arr[0]
        b = arr[1]
        lcm = a*b//math.gcd(a, b)
        arr.pop(0)
        arr.pop(0)
        arr.append(lcm)
    return lcm