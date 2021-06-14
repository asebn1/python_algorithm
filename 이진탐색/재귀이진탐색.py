
def binary_search(array, target, start, end):
    if start > end:
        return
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)

# 타겟 입력
target = int(input())
# 리스트 입력
array = list(map(int, input()))

print(binary_search(array, target, 0, len(array)-1)+1)