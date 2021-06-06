n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(d[0], array[1])

for i in range(2, n):
    d[i] = max(array[i]+d[i-2], d[i-1])
print(d[n-1])