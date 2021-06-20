array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    
    while 1:
        if left > right:
            break
        # 1. 처음 피벗 5에서 비교
        # 2. left에서 시작. 피벗 5보다 큰 위치 찾음 (오른쪽 넘김) -> 7
        while left <= end and array[left] <= array[pivot]:
            left += 1 
        # 3. right에서 시작. 피벗 5보다 작은 위치 찾음(왼쪽 넘김) -> 4
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 5. 다 했으면 교환 후 종료
            array[right], array[pivot] = array[pivot], array[right]
        else: # 4. 7과 4 교환. 
            array[left], array[right] = array[right], array[left]

    # 재귀
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)