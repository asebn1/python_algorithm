def match(arr, key, rot, r, c):
    M = len(key)
    # arr에 key 삽입
    for i in range(M):
        for j in range(M):
            if rot == 0:
                arr[r+i][c+j] += key[i][j]
            # 90
            elif rot == 1:
                arr[r+i][c+j] += key[M-1-j][i]
            # 180
            elif rot == 2:
                arr[r+i][c+j] += key[M-1-i][M-1-j]
            # 270
            elif rot == 3:
                arr[r+i][c+j] += key[j][M-1-i]

# 체크함수
def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    # 떨어진 거리. 1개는 겹쳐야 하므로
    offset = M - 1 # 2
    for r in range(offset + N):
        for c in range(offset + N):
            # 4번 0, 90, 180, 270
            for rot in range(4):
                # 58 * 58 배열. 비교대상
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(N):
                    for j in range(N):
                        # 초기화된 arr에 lock 입력
                        arr[offset+i][offset+j] = lock[i][j]
                # key 대입
                match(arr, key, rot, r, c)
                # 체크
                # arr의 lock 부분 전부 1?
                if check(arr, offset, N):
                    return True
    return False