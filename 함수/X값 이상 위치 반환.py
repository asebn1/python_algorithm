# 5 이상 값 위치 반환
def solution(x, arr):
    # 이진법
    start, end = 0, len(arr)
    while start != end and start != len(arr):
        if arr[(start+end)//2] >= x:
            end = (start+end) // 2
        else:
            start = (start+end) // 2 + 1
    # 해당 인덱스 부터 끝까지 개수가 정답
    return start

x = 5
arr = [1,3,4,7,9,11, 13, 15,17]
print(solution(x, arr))