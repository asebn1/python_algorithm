import heapq


def solution(scoville, K):
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    cnt = 0
    while q[0] < K:
        if len(q) < 2:
            break
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        cnt += 1

        heapq.heappush(q, a + b * 2)
    if heapq.heappop(q) < K:
        return -1
    return cnt


"""
1. 정렬

2. 만약 db[0] >= k:
    break
elif len(db) >= 2:
식 적용
"""