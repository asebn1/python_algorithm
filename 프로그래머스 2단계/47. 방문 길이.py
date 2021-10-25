def solution(dirs):
    visited = [[[False] * 4 for _ in range(11)] for _ in range(11)]
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    idx, idy = 5, 5
    answer = 0

    for i in dirs:
        plus_idx, plus_idy = -1, -1
        temp = 0
        temp2 = 0
        if i == 'U':
            temp = 0
            temp2 = 1
        elif i == 'D':
            temp = 1
            temp2 = 0
        elif i == 'L':
            temp = 2
            temp2 = 3
        elif i == 'R':
            temp = 3
            temp2 = 2
        # 범위 안에 있다면 값 추가

        if 0 <= idx + dx[temp] < 11 and 0 <= idy + dy[temp] < 11:
            plus_idx = idx + dx[temp]
            plus_idy = idy + dy[temp]
            print(plus_idx, plus_idy, temp)

        # 방문 체크. 방문한 적 없으면 추가(양쪽)
        if (plus_idx != -1) and visited[plus_idx][plus_idy][temp] == False:
            if temp == 0:
                visited[plus_idx][plus_idy][temp] = True
                visited[plus_idx - 1][plus_idy][temp2] = True
            elif temp == 1:
                visited[plus_idx][plus_idy][temp] = True
                visited[plus_idx + 1][plus_idy][temp2] = True
            elif temp == 2:
                visited[plus_idx][plus_idy][temp] = True
                visited[plus_idx][plus_idy + 1][temp2] = True
            elif temp == 3:
                visited[plus_idx][plus_idy][temp] = True
                visited[plus_idx][plus_idy - 1][temp2] = True

            answer += 1
        if (plus_idx != -1):
            idx = plus_idx
            idy = plus_idy

    return answer