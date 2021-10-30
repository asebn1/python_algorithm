from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    distance = [0] * 1000000
    distance[0] = -1
    i = 1
    while q:
        if len(q) == 0:
            break
        pop = q.popleft()

        cnt = 0
        j = 0
        while 1:
            if cnt == bridge_length:  # 2번
                break
            # 4
            if distance[i + j] + pop <= weight:
                distance[i + j] += pop
                cnt += 1
            j += 1
        i += j - cnt + 1
    return distance.index(0)


"""
7 4 5 6

0 1 2 3 4 5 6 7 8 9 
  7 7 4 4 5 6 6 끝
        5
        9

"""