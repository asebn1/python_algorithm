from itertools import permutations


def solution(n, weak, dist):
    # 순열
    arr = []
    for i in permutations(dist, len(dist)):
        arr.append(list(i))

    # [1, 5, 6, 10, 13, 17, 18, 22]
    # 시계방향으로만 확인
    weaksize = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = 10000

    # [1, 5, 6, 10, 13, 17, 18, 22]
    for start in range(weaksize):
        # 순열
        # 1,2,3,4 부터
        for d in arr:
            cnt = 1
            pos = start

            for i in range(1, weaksize):
                nextPos = start + i
                # 사이의 거리
                diff = weak[nextPos] - weak[pos]
                # 거리 넘으면
                if diff > d[cnt - 1]:
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)

    if minCnt == 10000:
        return -1

    return minCnt