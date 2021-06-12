n = int(input())
arr = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))
# 이진 검색

temp = False
def binary_search(arr, target, start, end):
    global temp
    if start > end:
        return
    mid = (start+end) // 2
    if arr[mid] == target:
        temp = True
    elif arr[mid] > target:
        binary_search(arr, target, start, mid-1)
    else:
        binary_search(arr, target, mid+1, end)

arr.sort()
for i in range(m):
    binary_search(arr, search[i], 0, n-1)
    if temp == True:
        print("yes", end=' ')
        temp = False
    else:
        print("no", end=' ')

print(search)
