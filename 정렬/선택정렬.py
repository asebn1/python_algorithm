# 한번 돌때마다 가장 작은값 왼쪽에 저장됨 (오름차순)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스왑
    array[min_index], array[i] = array[i], array[min_index]

print(array)
