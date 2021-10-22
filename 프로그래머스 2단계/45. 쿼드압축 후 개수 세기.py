def solution(arr):
    answer = [0, 0]
    n = len(arr)

    # 검사
    def check(x, y, n):
        # 기본 초기값
        init = arr[x][y]  # 0 or 1

        noInit = True
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    noInit = False
                    break
        # 같지 않으면 분할함
        if noInit == False:
            nn = n // 2
            # 0,0,4
            check(x, y, nn)
            check(x + nn, y, nn)
            check(x, y + nn, nn)
            check(x + nn, y + nn, nn)
        # 다 같으면 값 추가
        else:
            answer[init] += 1

    check(0, 0, n)  # 검사

    return answer