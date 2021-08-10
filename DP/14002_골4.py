# 백준 14002
n = int(input())
arr = list(map(int, input().split()))

arr = [0] + arr
dp = [0] + [1]*(n)

for i in range(1, n+1):
    for j in range(1, i+1): # 1~6
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
result = []
offset = max(dp)
for i in range(n, 0, -1):
    if dp[i] == offset:
        result.append(arr[i])
        offset -= 1
result.reverse()
for i in result:
    print(i, end=' ')