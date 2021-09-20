def solution(stones, k):
    left = 0
    right = max(stones)
    mid = 0
    while left <= right:
        mid = (left+right) // 2
        blank_cnt = 0
        for i in stones:
            if i-mid <= 0:
                blank_cnt += 1
            else:
                blank_cnt = 0
            if blank_cnt >= k:
                break
        if blank_cnt < k:
            left = mid + 1
        else:
            right = mid -1
    return left