def solution(n, times):
    right = min(times) * n  # 42
    left = 1
    answer = 0
    while (left <= right):
        mid = (left + right) // 2  # 21
        temp = n

        for time in times:
            temp -= mid // time  # 3,2
            if temp <= 0:
                answer = mid
                right = mid - 1
                break
        if temp > 0:
            left = mid + 1
    return answer