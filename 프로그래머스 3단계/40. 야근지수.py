import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    q = []
    for i in works:
        heapq.heappush(q, -i)
    for i in range(n):
        pop = heapq.heappop(q)
        heapq.heappush(q, pop + 1)
    result = 0
    for i in q:
        result += i ** 2
    return result


"""
야근 피로도 = 야근시작시점, 남은일 ** 2
"""