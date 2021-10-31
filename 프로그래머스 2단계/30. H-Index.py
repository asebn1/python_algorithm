from bisect import bisect_left, bisect_right
def solution(citations):
    citations.sort()
    db = [0] + citations
    n = len(citations)
    h = 0
    print(db)
    for i in range(1, n+1):
        # h번 이상 인용된 논문이 h편 이상
        if i <= n-bisect_left(db, i)+1 and i >= n-bisect_left(db, i):
            h = i

    return h