def solution(m, n, board):
    answer = 0
    array = [[' '] * n for _ in range(m)]
    # 1차원 -> 2차원 재설정
    for i in range(m):
        for j in range(n):
            array[i][j] = (board[i])[j]
    while 1:
        # 삭제되는 것이 없을때까지
        check = False

        # 겹치는 것에 '-' 추가함
        for y in range(m - 1):
            for x in range(n - 1):
                if (array[y][x])[0] == '0':
                    continue
                elif ((array[y][x])[0] == (array[y + 1][x])[0]) and ((array[y][x])[0] == (array[y][x + 1])[0]) and (
                        (array[y][x])[0] == (array[y + 1][x + 1])[0]):
                    if len(array[y][x]) == 1:
                        array[y][x] += '-'
                    if len(array[y][x + 1]) == 1:
                        array[y][x + 1] += '-'
                    if len(array[y + 1][x]) == 1:
                        array[y + 1][x] += '-'
                    if len(array[y + 1][x + 1]) == 1:
                        array[y + 1][x + 1] += '-'

        # '-' 있는 것 삭제
        for i in range(m):
            for j in range(n):
                if len(array[i][j]) == 2:
                    array[i][j] = '0'
                    # 삭제된 수 카운트
                    answer += 1
                    check = True

        # 밑으로 밀기
        for k in range(n):
            for i in range(m - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    if array[i][k] == '0' and array[j][k] != '0':
                        array[i][k], array[j][k] = array[j][k], array[i][k]

        if check == False:
            break

    return answer