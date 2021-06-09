n, m = map(int, input().split())
d = [10001] * (m+1)
array = []
for _ in range(n):
    array.append(int(input()))

# 1. 배수만큼 저장
for i in range(0, len(array)):
    for j in range(1, m+1):
        if j % array[i] == 0:
            d[j] = int(j/array[i])

# 각 array만큼 더했을 때 적은 값 저장
for i in range(0, len(array)):
    for j in range(1, m+1):
        if (j + array[i]) <= m:
            d[j + array[i]] = min(d[j + array[i]], d[j]+1)
if d[-1] == 10001:
    print(-1)
else:
    print(d[-1])