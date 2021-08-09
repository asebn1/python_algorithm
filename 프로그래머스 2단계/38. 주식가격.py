from bisect import bisect_left
def solution(prices):
    n = len(prices)
    result = [0]*n
    for i in range(0, n):
        cnt = 0
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        result[i] = cnt
    return result