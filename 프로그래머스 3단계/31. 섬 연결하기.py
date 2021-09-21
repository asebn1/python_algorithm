def solution(n, costs):
    visited = [False] * n
    costs.sort(key=lambda x: x[2])

    answer = 0
    visited[costs[0][0]] = True
    while 1:
        if False not in visited:
            break
        for i in costs:
            x, y, dist = i[0], i[1], i[2]
            # print(dist, x, y)
            if visited[x] == False and visited[y] == False:
                continue

            if visited[x] == False or visited[y] == False:
                visited[x] = True
                visited[y] = True
                answer += dist
                break
    return answer


# print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))
"""
01 1

"""